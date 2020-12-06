from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputFile

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

files_paths = ['/media/shared/Images/sticker.jpeg', '/media/shared/Images/Darjeeling1.png'] # пути к файлам


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Здесь ты помощи не найдешь, страдай!")


@dp.message_handler(content_types=['photo'])
async def echo_image(msg: types.Message):
    await msg.reply("Файл загружен, добавьте следующий или завершите работу.")

    file_id = msg['photo'][-1]['file_id']
    # здесь нужно скачать файл в папку и получить путь к файлу
    path = None
    if msg.from_user.id in files_paths.keys():
        files_paths[msg.from_user.id].append(path)
    else:
        files_paths[msg.from_user.id] = [path]

    # await bot.send_photo(msg.from_user.id, aaa)


@dp.message_handler(commands=['finish'])
async def finish_uploading(msg: types.Message):
    await msg.reply("Файлы загружены, ожидайте обработки.")
    for path in files_paths:
            file = InputFile(path)
            await bot.send_photo(msg.from_user.id, file)


if __name__ == '__main__':
    executor.start_polling(dp)
