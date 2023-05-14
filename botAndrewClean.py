from aiogram import Bot, types

from aiogram.dispatcher import Dispatcher

from aiogram.utils import executor

bot = Bot('YOUR TOKEN')

dp = Dispatcher(bot)


@dp.message_handler(commands='denis')
async def cmdtest(msg: types.Message):
    with open('leontiev.jpg', 'rb') as photo:
        await msg.answer_photo(photo)


@dp.message_handler(commands='aboba')
async def cmdtest(msg: types.Message):
    with open('leontiev2.jpg', 'rb') as photo:
        await msg.answer_photo(photo)

@dp.message_handler(commands='sunglasses')
async def cmdtest(msg: types.Message):
    with open('sunglasses.jpg', 'rb') as photo:
        await msg.answer_photo(photo)




if __name__ == '__main__':
    executor.start_polling(dp)