from aiogram import Bot, types

from aiogram.dispatcher import Dispatcher

from aiogram.utils import executor

bot = Bot('6219283718:AAHxN-6XznrX4uc6PyFSja0dp_h_EcOH6Pk')

dp = Dispatcher(bot)


@dp.message_handler(commands='denis')
async def cmdtest(msg: types.Message):
    with open('leontiev.jpg', 'rb') as photo:
        await msg.answer_photo(photo)


@dp.message_handler(commands='aboba')
async def cmdtest(msg: types.Message):
    with open('leontiev2.jpg', 'rb') as photo:
        await msg.answer_photo(photo)




if __name__ == '__main__':
    executor.start_polling(dp)