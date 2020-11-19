import time
import logging
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.utils.emoji import emojize
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Contact, Location
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from buttons import *
from db import *
from classes import Users, Form


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
users = {}


@dp.message_handler(commands=['start'])
async def hello(msg: types.Message):
    await bot.send_message(msg.from_user.id, f"Прекрасный день для закупок {msg.from_user.first_name}!", 'Согласен?', reply_markup=menu_btns)
    global id_
    id_ = msg.from_user.id
    users[id_] = Users(f'{id_}')
    await Form.starting.set()

@dp.message_handler(content_types=['photo'])
async def get_photo(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Фото сохранено в базу')
    print(msg)


@dp.message_handler(state=Form.starting)
async def func_menu(msg: types.Message, state: FSMContext):
    if msg.text == 'Меню':
        await bot.send_photo(msg.from_user.id, ol2, reply_markup=menu_btns1 )
        await Form.first_step.set()      #шаг.

    elif msg.text == 'Единоборства:':
        await bot.send_photo(msg.from_user.id, p1 ,  'TWINS', reply_markup=btns1)
        time.sleep(1)
        await bot.send_photo(msg.from_user.id, p2, 'VENUM-(яд)', reply_markup=btns2)
        time.sleep(1)
        await bot.send_photo(msg.from_user.id, p3, 'WALON', reply_markup=btns3)

    elif msg.text == 'Протеины:':
        await bot.send_message(msg.from_user.id,  'Протеин 1', reply_markup=btns1)
        time.sleep(1)
        await  bot.send_message(msg.from_user.id, 'Протеин 2', reply_markup=btns2)
        time.sleep(1)
        await bot.send_message(msg.from_user.id, 'Протеин 3', reply_markup=btns3)

    elif msg.text == 'Корзина':
        await bot.send_message(msg.from_user.id, 'Ваша корзина: ')
        for element in users[id_]:
            await bot.send_message(msg.from_user.id, element)

    elif msg.text == 'Как связатся?':
        await bot.send_message(msg.from_user.id, 'Вы можете обратиться по контактному номеру ввотсап! \n'
                                                 '+996507110303 - Маркет INIT.KG' )
    await Form.second_step()

    # if msg.text == 'Главное меню: ':
    #     await bot.send_message(msg.from_user.id, 'Главное меню', reply_markup=menu_btns)


@dp.callback_query_handler(state=Form.second_step.set())
async def show_description(call: types.CallbackQuery):
    msg = call.data
    if msg == 'desc1':
        await bot.send_message(call.from_user.id, deks_text )
    elif msg == 'desc2':
        await bot.send_message(call.from_user.id, desk_text2)
    elif msg == 'desc3':
        await bot.send_message(call.from_user.id, desk_text3)

    elif msg == 'add1':
        users[id_].append('Боксерские перчатки/проффесиональные.')
    elif msg == 'add2':
        users[id_].append('Боксерские перчатки/проффесиональные.')
    elif msg == 'add3':
        users[id_].append('Боксерские перчатки/проффесиональные.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

