# kavk_api
Krindra's асинхронный модуль Python для скриптов c использованием API vk.com

###### (я бы свой ник в начало не поставил, если бы меня пускали с именем avk_api на pypi.org , но нет. Пайпи сосите хуй)

## Установка
```pip install kavk-api```

## Пример
```python
import asyncio
from avk_api import Vk
from user_longpoll import LongPoll

async def main():
  vk = Vk('token')
  api = vk.get_api()
  longpoll = LongPoll(vk)
  await api.wall.post(message="Привет kavk_api!")
  async for event in longpoll.listen():
      print(event)
      
  
asyncio.run(main())
```


# Огромное спасибо:
### [python273](https://github.com/python273) за вдохновение и за то что я спиздил у вас код
