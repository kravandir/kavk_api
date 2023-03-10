from avk_api import Vk, BotLongPoll, BotEventType
import os
import asyncio

async def main():
    vk = Vk(token=os.environ['TOKEN'])
    lp = BotLongPoll(vk)
    async for event in lp.listen():
        if event.type == BotEventType.MESSAGE_NEW:
            obj = event.obj['message']
            print("новое сообщение от: ", obj['from_id'])
            print('Текст: ', obj['text'])

asyncio.run(main())
