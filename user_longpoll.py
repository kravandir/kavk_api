from avk_api import Vk
from exceptions import LPError
from enum import IntEnum

class VkEventType(IntEnum):
    """ Перечисление событий, получаемых от longpoll-сервера.
    `Подробнее в документации VK API
    <https://vk.com/dev/using_longpoll?f=3.+Структура+событий>`
    взято из vk_api от python273
    """

    #: Замена флагов сообщения (FLAGS:=$flags)
    MESSAGE_FLAGS_REPLACE = 1
    #: Установка флагов сообщения (FLAGS|=$mask)
    MESSAGE_FLAGS_SET = 2

    #: Сброс флагов сообщения (FLAGS&=~$mask)
    MESSAGE_FLAGS_RESET = 3

    #: Добавление нового сообщения.
    MESSAGE_NEW = 4

    #: Редактирование сообщения.
    MESSAGE_EDIT = 5

    #: Прочтение всех входящих сообщений в $peer_id,
    #: пришедших до сообщения с $local_id.
    READ_ALL_INCOMING_MESSAGES = 6

    #: Прочтение всех исходящих сообщений в $peer_id,
    #: пришедших до сообщения с $local_id.
    READ_ALL_OUTGOING_MESSAGES = 7

    #: Друг $user_id стал онлайн. $extra не равен 0, если в mode был передан флаг 64.
    #: В младшем байте числа extra лежит идентификатор платформы
    #: (см. :class:`VkPlatform`).
    #: $timestamp — время последнего действия пользователя $user_id на сайте.
    USER_ONLINE = 8

    #: Друг $user_id стал оффлайн ($flags равен 0, если пользователь покинул сайт и 1,
    #: если оффлайн по таймауту). $timestamp — время последнего действия пользователя
    #: $user_id на сайте.
    USER_OFFLINE = 9

    #: Сброс флагов диалога $peer_id.
    #: Соответствует операции (PEER_FLAGS &= ~$flags).
    #: Только для диалогов сообществ.
    PEER_FLAGS_RESET = 10

    #: Замена флагов диалога $peer_id.
    #: Соответствует операции (PEER_FLAGS:= $flags).
    #: Только для диалогов сообществ.
    PEER_FLAGS_REPLACE = 11

    #: Установка флагов диалога $peer_id.
    #: Соответствует операции (PEER_FLAGS|= $flags).
    #: Только для диалогов сообществ.
    PEER_FLAGS_SET = 12

    #: Удаление всех сообщений в диалоге $peer_id с идентификаторами вплоть до $local_id.
    PEER_DELETE_ALL = 13

    #: Восстановление недавно удаленных сообщений в диалоге $peer_id с
    #: идентификаторами вплоть до $local_id.
    PEER_RESTORE_ALL = 14

    #: Один из параметров (состав, тема) беседы $chat_id были изменены.
    #: $self — 1 или 0 (вызваны ли изменения самим пользователем).
    CHAT_EDIT = 51

    #: Изменение информации чата $peer_id с типом $type_id
    #: $info — дополнительная информация об изменениях
    CHAT_UPDATE = 52

    #: Пользователь $user_id набирает текст в диалоге.
    #: Событие приходит раз в ~5 секунд при наборе текста. $flags = 1.
    USER_TYPING = 61

    #: Пользователь $user_id набирает текст в беседе $chat_id.
    USER_TYPING_IN_CHAT = 62

    #: Пользователь $user_id записывает голосовое сообщение в диалоге/беседе $peer_id
    USER_RECORDING_VOICE = 64

    #: Пользователь $user_id совершил звонок с идентификатором $call_id.
    USER_CALL = 70

    #: Счетчик в левом меню стал равен $count.
    MESSAGES_COUNTER_UPDATE = 80

    #: Изменились настройки оповещений.
    #: $peer_id — идентификатор чата/собеседника,
    #: $sound — 1/0, включены/выключены звуковые оповещения,
    #: $disabled_until — выключение оповещений на необходимый срок.
    NOTIFICATION_SETTINGS_UPDATE = 114

class Event:
    def __init__(self, event_raw:dict):
        self.raw = event_raw
        self.type = VkEventType(event_raw[0])
        #TODO

        

class LongPoll:
    def __init__(self, vk:Vk, wait:int=25, mode:int=2, v:int=3) -> None:
        self._vk = vk
        self._api = vk.get_api()
        self._wait = wait
        self._mode = mode
        self._v = v
        self.params = None

    async def listen(self):
        while 1:
            async for event in LongPoll(self._vk, self._wait, self._mode, self._v):
                yield event
    
    # Что происходит дальше?
    # __aiter__ возвращает коду `async for e in LongPoll.listem()`
    # функцию __anext__.
    # Она же в свою очередь просто получает наш новый ивент

    def __aiter__(self): return self

    async def __anext__(self):
        if not self.params: 
            r = await self._api.messages.getLongPollServer(lp_version=self._v)
            print(r)
            self.params = {'key': r['key'], 'ts': r['ts'],
                           'wait': self._wait, 'mode': self._mode,
                           'version': self._v, 'act': 'a_check'}
            self.server = 'https://'+r['server']

        async with self._vk.client.get(url=self.server, params=self.params) as r:
            # r = await self._vk.client.get(url=self.server, params=self.params)
            r = await r.json()
            self.params.update({'ts': r['ts']})
            try:
                e = r['failed']
                if e != 1: raise LPError(e)
                else: return
            except:
                pass
            #TODO: ВОЗВРАТ КЛАССА ИВЕНТ
            return r['updates']

