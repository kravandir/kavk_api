# avk_api
Asynchronus VK API

## Example
```python
import asyncio
from avk_api import Vk
from user_longpoll import LongPoll

async def main():
  vk = Vk('token')
  api = vk.get_api()
  longpoll = LongPoll(vk)
  vk.wall.post(message="Привет avk_api!")
  async for event in longpoll.listen():
      print(event)
      
```
