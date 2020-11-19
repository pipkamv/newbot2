from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from buttons import *
from db import *
from classes import Users, Form


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)





@dp.message_handler(content_types=['photo'])
async def get_photo(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Фото сохранено в базу')
    print(msg)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
