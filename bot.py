from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputFile

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

save_path = 'D:/pictures/'
files_paths = dict()


async def evaluate(path):
    # TODO
    return path


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Здесь ты помощи не найдешь, страдай!")


@dp.message_handler(content_types=['photo'])
async def echo_image(msg: types.Message):
    file_id = msg['photo'][-1]['file_id']
    path = save_path + file_id + '.jpg'
    await msg.reply("Файл загружен, добавьте следующий или завершите работу.")
    await msg.photo[-1].download(path)
    path = await path
    if msg.from_user.id in files_paths.keys():
        files_paths[msg.from_user.id].append(path)
    else:
        files_paths[msg.from_user.id] = [path]

    # await bot.send_photo(msg.from_user.id, aaa)


@dp.message_handler(commands=['finish'])
async def finish_uploading(msg: types.Message):
    await msg.reply("Ожидайте обработки.")
    for path in files_paths[msg.from_user.id]:
        file = InputFile(path)
        await bot.send_photo(msg.from_user.id, file)


if __name__ == '__main__':
    executor.start_polling(dp)
