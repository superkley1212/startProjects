import os
import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile
from aiogram.utils import executor
# from PIL import Image

# ваш токен бота
TOKEN = "token"

# создание экземпляра бота
bot = Bot(TOKEN)
dp = Dispatcher(bot)

# функция отправки случайного фото
async def send_random_photo(chat_id):
    # путь к папке с фото
    photo_folder = "./leonov"
    # список файлов в папке
    file_list = os.listdir(photo_folder)
    # выбор случайного файла
    photo_name = random.choice(file_list)
    # полный путь к файлу
    photo_path = os.path.join(photo_folder, photo_name)
    # загрузка фото в сообщение
    with open(photo_path, "rb") as photo_file:
        photo = InputFile(photo_file)
        await bot.send_photo(chat_id, photo)

# хендлер для команды /random_photo
@dp.message_handler(commands=['random_photo'])
async def cmd_random_photo(message: types.Message):
    # отправка случайного фото
    await send_random_photo(message.chat.id)

# запуск бота
if __name__ == '__main__':
    executor.start_polling(dp)

#
# нерабочий код, зашел в тупик при его написании
#
# from aiogram import Bot, types
# import codecs
# from aiogram.dispatcher import Dispatcher
#
# from aiogram.utils import executor
# import random
# import os
#
# bot = Bot('your token')
#
# dp = Dispatcher(bot)
# fileObj = codecs.open( "E:\Python\PycharmProjects\pythonProject\\futurecode\\botLeontiev\photoLeonov", "r", "utf_8_sig" )
# # DIR = 'E:\Python\PycharmProjects\pythonProject\\futurecode\\botLeontiev\photoLeonov'
# @dp.message_handler(commands='rp')
# async def cmdtest(msg: types.Message):
#     with open(os.path.join(fileObj, random.choice(os.listdir(fileObj)))) as photo:
#         await msg.answer_photo(photo)
#
#
# @dp.message_handler(commands='denis')
# async def cmdtest(msg: types.Message):
#     with open('leontiev.jpg', 'rb') as photo:
#         await msg.answer_photo(photo)
#
#
# @dp.message_handler(commands='aboba')
# async def cmdtest(msg: types.Message):
#     with open('leontiev2.jpg', 'rb') as photo:
#         await msg.answer_photo(photo)
#
# @dp.message_handler(commands='sunglasses')
# async def cmdtest(msg: types.Message):
#     with open('sunglasses.jpg', 'rb') as photo:
#         await msg.answer_photo(photo)
#
#
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp)
# нерабочий код, зашел в тупик при его написании
#
#
#