'''
Большинство enum взято из https://github.com/python273/vk_api/
Автор: python273
'''
from enum import IntEnum


CHAT_START_ID = int(2E9)  # id с которого начинаются беседы


class VkLongpollMode(IntEnum):
    """ Дополнительные опции ответа
    `Подробнее в документации VK API
    <https://vk.com/dev/using_longpoll?f=1.+Подключение>`_
    """

    #: Получать вложения
    GET_ATTACHMENTS = 2

    #: Возвращать расширенный набор событий
    GET_EXTENDED = 2**3

    #: возвращать pts для метода `messages.getLongPollHistory`
    GET_PTS = 2**5

    #: В событии с кодом 8 (друг стал онлайн) возвращать
    #: дополнительные данные в поле `extra`
    GET_EXTRA_ONLINE = 2**6

    #: Возвращать поле `random_id`
    GET_RANDOM_ID = 2**7


DEFAULT_MODE = sum(VkLongpollMode)


class VkEventType(IntEnum):
    """ Перечисление событий, получаемых от longpoll-сервера.
    `Подробнее в документации VK API
    <https://vk.com/dev/using_longpoll?f=3.+Структура+событий>`__
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


class VkPlatform(IntEnum):
    """ Идентификаторы платформ """

    #: Мобильная версия сайта или неопознанное мобильное приложение
    MOBILE = 1

    #: Официальное приложение для iPhone
    IPHONE = 2

    #: Официальное приложение для iPad
    IPAD = 3

    #: Официальное приложение для Android
    ANDROID = 4

    #: Официальное приложение для Windows Phone
    WPHONE = 5

    #: Официальное приложение для Windows 8
    WINDOWS = 6

    #: Полная версия сайта или неопознанное приложение
    WEB = 7


class VkOfflineType(IntEnum):
    """ Выход из сети в событии :attr:`VkEventType.USER_OFFLINE` """

    #: Пользователь покинул сайт
    EXIT = 0

    #: Оффлайн по таймауту
    AWAY = 1


class VkMessageFlag(IntEnum):
    """ Флаги сообщений """

    #: Сообщение не прочитано.
    UNREAD = 1

    #: Исходящее сообщение.
    OUTBOX = 2

    #: На сообщение был создан ответ.
    REPLIED = 2**2

    #: Помеченное сообщение.
    IMPORTANT = 2**3

    #: Сообщение отправлено через чат.
    CHAT = 2**4

    #: Сообщение отправлено другом.
    #: Не применяется для сообщений из групповых бесед.
    FRIENDS = 2**5

    #: Сообщение помечено как "Спам".
    SPAM = 2**6

    #: Сообщение удалено (в корзине).
    DELETED = 2**7

    #: Сообщение проверено пользователем на спам.
    FIXED = 2**8

    #: Сообщение содержит медиаконтент
    MEDIA = 2**9

    #: Приветственное сообщение от сообщества.
    HIDDEN = 2**16

    #: Сообщение удалено для всех получателей.
    DELETED_ALL = 2**17


class VkPeerFlag(IntEnum):
    """ Флаги диалогов """

    #: Важный диалог
    IMPORTANT = 1

    #: Неотвеченный диалог
    UNANSWERED = 2


class VkChatEventType(IntEnum):
    """ Идентификатор типа изменения в чате """

    #: Изменилось название беседы
    TITLE = 1

    #: Сменилась обложка беседы
    PHOTO = 2

    #: Назначен новый администратор
    ADMIN_ADDED = 3

    #: Изменены настройки беседы
    SETTINGS_CHANGED = 4

    #: Закреплено сообщение
    MESSAGE_PINNED = 5

    #: Пользователь присоединился к беседе
    USER_JOINED = 6

    #: Пользователь покинул беседу
    USER_LEFT = 7

    #: Пользователя исключили из беседы
    USER_KICKED = 8

    #: С пользователя сняты права администратора
    ADMIN_REMOVED = 9

    #: Бот прислал клавиатуру
    KEYBOARD_RECEIVED = 11


MESSAGE_EXTRA_FIELDS = [
    'peer_id', 'timestamp', 'text', 'extra_values', 'attachments', 'random_id'
]
MSGID = 'message_id'

EVENT_ATTRS_MAPPING = {
    VkEventType.MESSAGE_FLAGS_REPLACE: [MSGID, 'flags'] + MESSAGE_EXTRA_FIELDS,
    VkEventType.MESSAGE_FLAGS_SET: [MSGID, 'mask'] + MESSAGE_EXTRA_FIELDS,
    VkEventType.MESSAGE_FLAGS_RESET: [MSGID, 'mask'] + MESSAGE_EXTRA_FIELDS,
    VkEventType.MESSAGE_NEW: [MSGID, 'flags'] + MESSAGE_EXTRA_FIELDS,
    VkEventType.MESSAGE_EDIT: [MSGID, 'mask'] + MESSAGE_EXTRA_FIELDS,

    VkEventType.READ_ALL_INCOMING_MESSAGES: ['peer_id', 'local_id'],
    VkEventType.READ_ALL_OUTGOING_MESSAGES: ['peer_id', 'local_id'],

    VkEventType.USER_ONLINE: ['user_id', 'extra', 'timestamp'],
    VkEventType.USER_OFFLINE: ['user_id', 'flags', 'timestamp'],

    VkEventType.PEER_FLAGS_RESET: ['peer_id', 'mask'],
    VkEventType.PEER_FLAGS_REPLACE: ['peer_id', 'flags'],
    VkEventType.PEER_FLAGS_SET: ['peer_id', 'mask'],

    VkEventType.PEER_DELETE_ALL: ['peer_id', 'local_id'],
    VkEventType.PEER_RESTORE_ALL: ['peer_id', 'local_id'],

    VkEventType.CHAT_EDIT: ['chat_id', 'self'],
    VkEventType.CHAT_UPDATE: ['type_id', 'peer_id', 'info'],

    VkEventType.USER_TYPING: ['user_id', 'flags'],
    VkEventType.USER_TYPING_IN_CHAT: ['user_id', 'chat_id'],
    VkEventType.USER_RECORDING_VOICE: ['peer_id', 'user_id', 'flags', 'timestamp'],

    VkEventType.USER_CALL: ['user_id', 'call_id'],

    VkEventType.MESSAGES_COUNTER_UPDATE: ['count'],
    VkEventType.NOTIFICATION_SETTINGS_UPDATE: ['values']
}


def get_all_event_attrs():
    keys = set()

    for l in EVENT_ATTRS_MAPPING.values():
        keys.update(l)

    return tuple(keys)


ALL_EVENT_ATTRS = get_all_event_attrs()

PARSE_PEER_ID_EVENTS = [
    k for k, v in EVENT_ATTRS_MAPPING.items() if 'peer_id' in v
]
PARSE_MESSAGE_FLAGS_EVENTS = [
    VkEventType.MESSAGE_FLAGS_REPLACE,
    VkEventType.MESSAGE_NEW
]
