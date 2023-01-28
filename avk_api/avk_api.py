from typing import Callable
import aiohttp, asyncio_atexit
from .exceptions import VkError

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

    def __getattr__(self, method:str):
        if '_' in method:
            m = method.split('_')
            method = m[0] + ''.join(i.title() for i in m[1:])

        return Api(
            self._vk,
            (self._method + '.' if self._method else '') + method
        )

    def __call__(self, **kwargs):
        for k, v in kwargs.items():
            if isinstance(v, (list, tuple)):
                kwargs[k] = ','.join(str(x) for x in v)

        return self._vk.call_method(self._method, **kwargs)





