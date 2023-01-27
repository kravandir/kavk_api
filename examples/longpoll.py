from avk_api import Vk, LongPoll, VkEventType
import os
import asyncio

async def main():
    vk = Vk(token=os.environ['TOKEN'])
    lp = LongPoll(vk)
    async for event in lp.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print("новое сообщение", end=" ")
            if event.from_me:
                print('От меня для: ', end='')
            elif event.to_me:
                print('Для меня от: ', end='')

            if event.from_user:
                print(event.user_id)
            elif event.from_chat:
                print(event.user_id, 'в беседе', event.chat_id)
            elif event.from_group:
                print('группы', event.group_id)

            print('Текст: ', event.text)

asyncio.run(main())
