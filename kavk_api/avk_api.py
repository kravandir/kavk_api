from typing import Callable
import aiohttp, asyncio_atexit
from .exceptions import VkError
from .types.methods import *

class Captcha:
    def __init__(self, captcha:dict) -> None:
        self.raw = captcha
        self.img = captcha['captcha_img']
        self.sid = captcha['captcha_sid']


def captcha_handler(captcha:Captcha) -> str:
    print(captcha)
    return ''


class Vk:
    def __init__(self, token:str, captcha_handler:Callable[[Captcha], str]=captcha_handler,
                url:str="https://api.vk.com/method/", version="5.131") -> None:
        self.token = token
        self.client = aiohttp.ClientSession(conn_timeout=60)
        self.captcha_handler = captcha_handler
        self.URL = url
        self.version = version
        self._params = {'access_token': self.token,
                        'v' : self.version}

        asyncio_atexit.register(self._on_exit)

    async def call_method(self, method:str, **params) -> dict:
        params.update(self._params)
        params = {k:v for k, v in params.items() if v is not None}
        async with self.client.get(self.URL+method, params=params) as r:
            r = await r.json()
            if self._check_for_error(r) > 0:
                code = self._check_for_error(r)
                if code == 14:
                    captcha = r['error']
                    captcha_key = self.captcha_handler(captcha)
                    try:
                        params.update({'captcha_sid': captcha.sid,
                                       'captcha_key': captcha_key})
                        r = await self.call_method(method, **params)
                        if self._check_for_error(r) > 0:
                            raise VkError(r['error'])
                    except: pass
                error = r['error']
                raise VkError(error)
            return r['response']

    def get_api(self):
        return Api(self)

    def _check_for_error(self, r:dict) -> int:
        try: 
            code = r['error']['error_code']
        except: code = 0
        finally: return code

    async def _on_exit(self) -> None:
        await self.client.close()


class Api:
    # взято из vk_api от python273
    def __init__(self, vk:Vk, method:str="") -> None:
        self._vk = vk
        self._method = method
        # Дальше скучно
        self.account = Account(vk)
        self.ads = Ads(vk)
        self.adsweb = Adsweb(vk)
        self.apps = Apps(vk)
        self.auth = Auth(vk)
        self.board = Board(vk)
        self.database = Database(vk)
        self.docs = Docs(vk)
        self.donut = Donut(vk)
        self.fave = Fave(vk)
        self.friends = Friends(vk)
        self.gifts = Gifts(vk)
        self.groups = Groups(vk)
        self.likes = Likes(vk)
        self.market = Market(vk)
        self.messages = Messages(vk)
        self.newsfeed = Newsfeed(vk)
        self.notes = Notes(vk)
        self.notifications = Notifications(vk)
        self.orders = Orders(vk)
        self.pages = Pages(vk)
        self.photos = Photos(vk)
        self.podcasts = Podcasts(vk)
        self.polls = Polls(vk)
        self.search = Search(vk)
        self.secure = Secure(vk)
        self.stats = Stats(vk)
        self.status = Status(vk)
        self.storage = Storage(vk)
        self.store = Store(vk)
        self.stories = Stories(vk)
        self.streaming = Streaming(vk)
        self.users = Users(vk)
        self.utils = Utils(vk)
        self.video = Video(vk)
        self.wall = Wall(vk)
        self.widgets = Widgets(vk)
        # Скука закончилась!


    def __getattr__(self, method:str):
        if '_' in method:
            m = method.split('_')
            method = m[0] + ''.join(i.title() for i in m[1:])

        return Api(
            self._vk,
            (self._method + '.' if self._method else '') + method
        )

    async def __call__(self, **kwargs):
        for k, v in kwargs.items():
            if isinstance(v, (list, tuple)):
                kwargs[k] = ','.join(str(x) for x in v)

        return await self._vk.call_method(self._method, **kwargs)





