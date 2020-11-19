from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.emoji import emojize

TOKEN = '1493574896:AAFAIvsN7OoE4TehsgYXY9o2C5JOLMy-sN0'


menu = KeyboardButton('Читать:')
cart = KeyboardButton('Оставить отзыв: ')
contacts = KeyboardButton('Как связатся?')


m1 = KeyboardButton('Викинги:')
m2 = KeyboardButton('Античный Рим:')
m3 = KeyboardButton('Самураи:')
m4 = KeyboardButton('Семь чудес света:')
m5 = KeyboardButton('Просто красивые места:')
m7 = KeyboardButton('Главное меню:')


menu_btns1 = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2).row(m1, m2, m3).add(m4).add(m5).add(m7)
menu_btns = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2).row(menu, cart).add(contacts)


add_to_cart1 = InlineKeyboardButton(text='Как появились?', callback_data='add1')
description1 = InlineKeyboardButton(text='Интересные факты:', callback_data='desc1')
pum = InlineKeyboardButton(text='Почитать больше', callback_data='pum')
btns1 = InlineKeyboardMarkup(row_width=2).row(add_to_cart1, description1).row(pum)



add_to_cart2 = InlineKeyboardButton(text='Как появились?', callback_data='add2')
description2 = InlineKeyboardButton(text='Интересные факты:', callback_data='desc2')
pum2 = InlineKeyboardButton(text='Почитать больше', callback_data='pum2')
btns2 = InlineKeyboardMarkup(row_width=2).row(add_to_cart2, description2).row(pum2)


add_to_cart3 = InlineKeyboardButton(text='Как появились?', callback_data='add3')
description3 = InlineKeyboardButton(text='Интересные факты: ', callback_data='desc3')
pum3 = InlineKeyboardButton(text='Почитать больше', callback_data='pum3')
btns3 = InlineKeyboardMarkup(row_width=2).row(add_to_cart3, description3).row(pum3)


add_interes = InlineKeyboardButton(text=emojize("Нравится :heart_eyes:"), callback_data='add4')
add_em = InlineKeyboardButton(text=emojize("Ну такое :thumbsdown:"), callback_data='desc4')
add_chit = InlineKeyboardButton(text='Посмотреть больше фотографий:', callback_data='fac1')
btns5 = InlineKeyboardMarkup(row_width=2).row(add_interes, add_em).add(add_chit)
btns6 = InlineKeyboardMarkup(row_width=2).row(add_interes, add_em)


kep1 = InlineKeyboardMarkup(text='7 чудес света в океане', callback_data = 'chudesa')
kep2 = InlineKeyboardMarkup(text='7 новых мировых чудес архитектуры', callback_data= 'chudesa2')
kep4 = InlineKeyboardMarkup(text='7 чудес  Древнего мира', callback_data ='chudesa4')
btns4 = InlineKeyboardMarkup(row_width=2).row(kep1).row(kep2).row(kep4)
