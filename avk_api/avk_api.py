import aiohttp, asyncio_atexit
from .exceptions import VkError

class Vk:
    def __init__(self, token:str, url:str="https://api.vk.com/method/",
                version="5.131") -> None:
        self.token = token
        self.client = aiohttp.ClientSession(conn_timeout=60)
        self.URL = url
        self.version = version
        self._params = {'access_token': self.token,
                        'v' : self.version}
        asyncio_atexit.register(self._on_exit)

    async def call_method(self, method:str, **params):
        params.update(self._params)
        async with self.client.get(self.URL+method, params=params) as r:
            r = await r.json()
            code = self._check_for_error(r)
            if code > 0:
                error = r['error']
                raise VkError(error)
            return r['response']

    def get_api(self):
        return Api(self)

    def _check_for_error(self, r:dict):
        try: 
            code = r['error']['error_code']
        except: code = 0
        finally: return code

    async def _on_exit(self):
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





