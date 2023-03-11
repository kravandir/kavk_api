from datetime import datetime
from .enums import *
from .kavk_api import Vk
from .exceptions import LPError

class Event(object):
    """ Событие, полученное от longpoll-сервера.
    Имеет поля в соответствии с `документацией
    <https://vk.com/dev/using_longpoll_2?f=3.%2BСтруктура%2Bсобытий>`_.
    События `MESSAGE_NEW` и `MESSAGE_EDIT` имеют (среди прочих) такие поля:
        - `text` - `экранированный <https://ru.wikipedia.org/wiki/Мнемоники_в_HTML>`_ текст
        - `message` - оригинальный текст сообщения.
    События с полем `timestamp` также дополнительно имеют поле `datetime`.
    """

    def __init__(self, raw:list):
        self.raw:list = raw

        self.from_user:bool = False
        self.from_chat:bool = False
        self.from_group:bool = False
        self.from_me:bool = False
        self.to_me:bool = False

        self.attachments:dict = {}

        self.message_id:int = 0
        self.timestamp:int = 0
        self.datetime:datetime = datetime(1,1,1)
        self.peer_id:int = 0
        self.flags:int= 0
        self.extra:int = 0
        self.extra_values:dict = {}
        self.type_id:int = 0
        self.values:dict = {}

        try:
            self.type = VkEventType(self.raw[0])
            self._list_to_attr(self.raw[1:], EVENT_ATTRS_MAPPING[self.type])
        except ValueError:
            self.type = self.raw[0]
        except IndexError:
            self.type = 0

        if self.extra_values:
            self._dict_to_attr(self.extra_values)

        if self.type in PARSE_PEER_ID_EVENTS:
            self._parse_peer_id()

        if self.type in PARSE_MESSAGE_FLAGS_EVENTS:
            self._parse_message_flags()

        if self.type is VkEventType.CHAT_UPDATE:
            self._parse_chat_info()
            try:
                self.update_type = VkChatEventType(self.type_id)
            except ValueError:
                self.update_type = self.type_id

        elif self.type is VkEventType.NOTIFICATION_SETTINGS_UPDATE:
            self._dict_to_attr(self.values)
            self._parse_peer_id()

        elif self.type is VkEventType.PEER_FLAGS_REPLACE:
            self._parse_peer_flags()

        elif self.type in [VkEventType.MESSAGE_NEW, VkEventType.MESSAGE_EDIT]:
            self._parse_message()

        elif self.type in [VkEventType.USER_ONLINE, VkEventType.USER_OFFLINE] and self.user_id != None:
            self.user_id = abs(self.user_id)
            self._parse_online_status()

        elif self.type is VkEventType.USER_RECORDING_VOICE:
            if isinstance(self.user_id, list):
                self.user_id = self.user_id[0]

        if self.timestamp:
            self.datetime = datetime.utcfromtimestamp(self.timestamp)

    def _list_to_attr(self, raw, attrs):
        for i in range(min(len(raw), len(attrs))):
            self.__setattr__(attrs[i], raw[i])

    def _dict_to_attr(self, values):
        for k, v in values.items():
            self.__setattr__(k, v)

    def _parse_peer_id(self):
        if isinstance(self.peer_id, int) and self.peer_id < 0:  # Сообщение от/для группы
            self.from_group = True
            self.group_id = abs(self.peer_id)

        elif isinstance(self.peer_id, int) and self.peer_id > CHAT_START_ID:  # Сообщение из беседы
            self.from_chat = True
            self.chat_id = self.peer_id - CHAT_START_ID

            if self.extra_values and 'from' in self.extra_values:
                self.user_id = int(self.extra_values['from'])

        else:  # Сообщение от/для пользователя
            self.from_user = True
            self.user_id = self.peer_id

    def _parse_message_flags(self):
        if isinstance(self.flags, int):
            self.message_flags = set(
                x for x in VkMessageFlag if self.flags & x
            )

    def _parse_peer_flags(self):
        if isinstance(self.flags, int):
            self.peer_flags = set(
                x for x in VkPeerFlag if self.flags & x
            )

    def _parse_message(self):
        if isinstance(self.flags, int):
            if self.type is VkEventType.MESSAGE_NEW:
                if self.flags & VkMessageFlag.OUTBOX:
                    self.from_me = True
                else:
                    self.to_me = True

        # ВК возвращает сообщения в html-escaped виде,
        # при этом переводы строк закодированы как <br> и не экранированы

        self.text = self.text.replace('<br>', '\n')
        self.message = self.text \
            .replace('&lt;', '<') \
            .replace('&gt;', '>') \
            .replace('&quot;', '"') \
            .replace('&amp;', '&')

    def _parse_online_status(self):
        try:
            if self.type is VkEventType.USER_ONLINE and self.extra != None:
                self.platform = VkPlatform(self.extra & 0xFF)

            elif self.type is VkEventType.USER_OFFLINE:
                self.offline_type = VkOfflineType(self.flags)

        except ValueError:
            pass

    def _parse_chat_info(self):
        if self.type_id == VkChatEventType.ADMIN_ADDED.value:
            self.info = {'admin_id': self.info}

        elif self.type_id == VkChatEventType.MESSAGE_PINNED.value:
            self.info = {'conversation_message_id': self.info}

        elif self.type_id in [VkChatEventType.USER_JOINED.value,
                              VkChatEventType.USER_LEFT.value,
                              VkChatEventType.USER_KICKED.value,
                              VkChatEventType.ADMIN_REMOVED.value]:
            self.info = {'user_id': self.info}


class LongPoll:
    def __init__(self, vk:Vk, wait:int=25, mode:int=2, v:int=3) -> None:
        self._vk = vk
        self._api = vk.get_api()
        self._wait = wait
        self._mode = mode
        self._v = v
        self.params = None

        self.updates = []

    async def listen(self):
        while 1:
            async for event in LongPoll(self._vk, self._wait, self._mode, self._v):
                yield event 

    async def get_event(self, url:str, params:dict) -> dict:
        r = await self._vk.client.get(url=url, params=params)
        r = await r.json()
        return r

    # Что происходит дальше?
    # __aiter__ возвращает коду `async for e in LongPoll.listem()`
    # функцию __anext__.
    # Она же в свою очередь просто получает наш новый ивент

    def __aiter__(self): return self

    async def __anext__(self) -> Event:
        if not self.params: 
            r = await self._api.messages.getLongPollServer(lp_version=self._v)
            self.params = {'key': r.key, 'ts': r.ts,
                           'wait': self._wait, 'mode': self._mode,
                           'version': self._v, 'act': 'a_check'}
            self.server = 'https://'+r.server

        if self.updates != []:
            u = self.updates.pop(0)
            return Event(u)
            
        r = await self.get_event(url=self.server, params=self.params)
        try:
            updates = r['updates']
        except IndexError:
            error = r['failed']
            if error == 1:
                self.params.update({'ts': r['ts']})
            elif error in (2,3):
                self.params = {}
            updates = [[0]]
        except Exception as e:
            raise e

        if len(updates) > 0:
            self.updates = updates[1:]
            update = updates[0]
        else:
            update = updates
        self.params.update({'ts': r['ts']})
        return Event(update)



