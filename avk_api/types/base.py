from abc import ABC
from pydantic import BaseModel as BM

class BaseMethod(ABC):
    def __init__(self, vk):
        self.vk = vk

    async def method(self, method:str, **params):
        try:
            params.pop('self')
        except: pass
        return await self.vk.call_method(method.lower(), **params)
