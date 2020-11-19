import time
import logging
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.emoji import emojize
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Contact, Location
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# from config import TOKEN, deks_text, desk_text2
from buttons import *
from db import *
from classes import Users, Form

from init_vol3_bot.buttons import menu_btns, menu_btns1, btns1, btns2, btns3, btns5, btns6
from init_vol3_bot.db import ol2, p1, p2, p3, chudo_sveta, myanma, kitay, ris, kambodga2, peru, japan, vetnam, \
    portugalia, USA, Turkish, bolivia, grezia, desk_text3, like, v1, r1, s1, rok, sem1, sem1_text, sem2, sem2_text, \
    sem3, sem3_text, sem4, sem5_text, sem5

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
users = {}


@dp.message_handler(commands=['start'])
async def hello(msg: types.Message):
    await bot.send_message(msg.from_user.id, f"Начнем читать {msg.from_user.first_name}?", reply_markup=menu_btns)
    global id_
    id_ = msg.from_user.id
    users[id_] = Users(f'{id_}')
    # await Form.starting.set()


@dp.message_handler(content_types=['photo'])
async def get_photo(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Фото сохранено в базу')
    print(msg)

#######################################################################################################################

@dp.message_handler(text='Читать:')#state=Form.starting)
@dp.message_handler(text='Оставить отзыв:')
@dp.message_handler(text='Как связатся?')
@dp.message_handler(text='Главное меню:')
async def func_menu(msg: types.Message): #):
    if msg.text == 'Читать:':
        await bot.send_photo(msg.from_user.id, ol2, reply_markup=menu_btns1 )

    elif msg.text == 'Оставить отзыв:':
        await bot.send_message(msg.from_user.id, '(Не обработано) Пиши сюда - kanamnkvk@mail.ru =)')
        # for element in users[id_]:
        #     await bot.send_message(msg.from_user.id, element)

    elif msg.text == 'Как связатся?':
        await bot.send_message(msg.from_user.id, 'Вы можете обратиться по контактному номеру ввотсап! \n'
                                                 '+996507110303 - Любитель читать Kana')
        # await Form.first_step.set()
    if msg.text== 'Главное меню:':
        await bot.send_message(msg.from_user.id, 'Главное меню', reply_markup=menu_btns)

#####################################################################################################################

@dp.message_handler(text='Посмотреть больше фотографий:')
@dp.message_handler(text='Викинги:')
@dp.message_handler(text='Античный Рим:')
@dp.message_handler(text='Самураи:')
@dp.message_handler(text='Семь чудес света:')
@dp.message_handler(text='Просто красивые места:')
async def func_menu1(klk: types.Message):
    if 'Викинги:' in klk.text:
        await bot.send_photo(klk.from_user.id, p1 , 'Да будет смерть моя! И воссторжествует дух мой в Вальхалле!', reply_markup=btns1)
        time.sleep(1)

    if 'Античный Рим:' in klk.text:
        await bot.send_photo(klk.from_user.id, p2, 'За короля жизнь отдам! За веру и семью!', reply_markup=btns2)
        time.sleep(1)

    if 'Самураи:' in klk.text:
        await bot.send_photo(klk.from_user.id, p3, 'Достижения господина цвели как сакура, теперь же я ронин...', reply_markup=btns3)

    if 'Семь чудес света:' in klk.text:
        await bot.send_photo(klk.from_user.id, chudo_sveta, 'Чудеса света касаются не только построек Древних времен, масшаб культуры человечества возрос в сотни, а-то и в тысячи раз. Морское дно тоже предлагает вам свои семь чудес света. Смотри!', reply_markup=btns4)


    if 'Просто красивые места:' in klk.text:
        await bot.send_photo(klk.from_user.id, myanma, '1.Баганы, Мьянма', reply_markup=btns5)
        time.sleep(2)
        await bot.send_photo(klk.from_user.id, kitay, '2. Цветные скалы Чжанъе Данксиа в провинции Ганьсу, Китай. Река Ли, Китай\n',reply_markup=btns5)
        time.sleep(2)
        await bot.send_photo(klk.from_user.id, ris, '3. Рисовые террасы в Му Кан Чай, Вьетнам', reply_markup=btns5)
        time.sleep(2)
        await bot.send_photo(klk.from_user.id, kambodga2, '4. Гигантский храмовый комплекс Ангкор-Ват, Камбоджа', reply_markup=btns5)
        time.sleep(2)
        await bot.send_photo(klk.from_user.id, peru, '5. Город инков Мачу-Пикчу, Перу', reply_markup=btns5)
        time.sleep(2)
        await bot.send_photo(klk.from_user.id, japan,  '6. Бамбуковый лес, Япония. Национальный приморский парк Хитачи',reply_markup=btns5)
        time.sleep(2)
        await bot.send_photo(klk.from_user.id, vetnam,  '7. Бухта Халонг в Тонкинском заливе, Вьетнам. Рисовые террасы в Му Кан Чай, Вьетнам', reply_markup=btns5)
        time.sleep(2)
        await bot.send_photo(klk.from_user.id, portugalia, '8. Морская пещера в Алгарве, Португалия',reply_markup=btns5)
        time.sleep(2)
        await bot.send_photo(klk.from_user.id, USA, '9. Долина Йосемити США', reply_markup=btns5)
        time.sleep(2)
        await bot.send_photo(klk.from_user.id, Turkish, '10. Памуккале (хлопковый замок) Турция', reply_markup=btns5)
        time.sleep(2)
        await bot.send_photo(klk.from_user.id, bolivia, '11. Салар де Юни: самый крупный солончак и одно из крупнейших зеркал в мире, Боливия', reply_markup=btns5)
        time.sleep(2)
        await bot.send_photo(klk.from_user.id, grezia, '12. Остров Санторини, Греция', reply_markup=btns5)



@dp.callback_query_handler()#state=Form.first_step)
async def show_description(call: types.CallbackQuery):
    msg = call.data
    if msg == 'desc1':
        await bot.send_message(call.from_user.id, deks_text )
    elif msg == 'desc2':
        await bot.send_message(call.from_user.id, desk_text2)
    elif msg == 'desc3':
        await bot.send_message(call.from_user.id, desk_text3)
    elif msg == 'add4':
        await bot.send_photo(call.from_user.id, like, f'Спасибо за положительный отзыв {call.from_user.first_name}!')
    elif msg == 'desc4':
        await bot.send_photo(call.from_user.id, like, f'Спасибо за отзыв {call.from_user.first_name}, будем стараться!')
    elif msg == 'pum':
        await bot.send_message(call.from_user.id )



    elif msg == 'add1':
        await bot.send_message(call.from_user.id, v1)
    elif msg == 'add2':
        await bot.send_message(call.from_user.id, r1)
    elif msg == 'add3':
        await bot.send_message(call.from_user.id, s1)
    elif msg == 'fac1':
        await bot.send_photo(call.from_user.id, rok, 'Яркие фотографии местостей https://cameralabs.org/5656-40-samykh-krasivykh-mest-na-zemle')



    elif msg == 'chudesa':
        await bot.send_photo(call.from_user.id, sem1, '1. Галапогосские острова', reply_markup=btns6)
        await bot.send_message(call.from_user.id, sem1_text)
        time.sleep(2)
        await bot.send_photo(call.from_user.id, sem2, '2. Красное море', reply_markup=btns6)
        await bot.send_message(call.from_user.id, sem2_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, sem3, '3. Палау' , reply_markup=btns6)
        await bot.send_message(call.from_user.id, sem3_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, sem4, '4. Белизский барьерный риф',reply_markup=btns6)
        await bot.send_message(call.from_user.id, sem5_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, sem5, '5. Озеро Байкал',reply_markup=btns6)
        await bot.send_message(call.from_user.id, sem5_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, sem6, '6. Большой барьерный риф',reply_markup=btns6)
        await bot.send_message(call.from_user.id, sem6_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, sem7, '7. Глубоководные морские трещины',reply_markup=btns6)
        await bot.send_message(call.from_user.id, sem7_text)


    elif msg =='chudesa2':
        await bot.send_photo(call.from_user.id, kem1, '1. Музей Гуггенхайма, Испания' ,reply_markup=btns6)
        await bot.send_message(call.from_user.id, kem1_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, kem2, '2. Башня Бурдж-Халифа, ОАЭ' , reply_markup=btns6)
        await bot.send_message(call.from_user.id, kem2_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, kem3, '3. Пекинский национальный стадион, Китай' ,reply_markup=btns6)
        await bot.send_message(call.from_user.id, kem3_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, kem4, '4. Дворец искусств королевы Софии, Испания' ,reply_markup=btns6)
        await bot.send_message(call.from_user.id, kem4_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, kem5, '5. Штаб квартира CCTV, Китай' , reply_markup=btns6)
        await bot.send_message(call.from_user.id, kem5_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, kem6, '6. Сиднейская опера, Австралия' ,reply_markup=btns6)
        await bot.send_message(call.from_user.id, kem6_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, kem7, '7. Сеент-Мэри Экс 30, Великобритания' ,reply_markup=btns6)
        await bot.send_message(call.from_user.id, kem7_text)


    elif msg == 'chudesa4':
        await bot.send_photo(call.from_user.id, bem, '1. Александрийский маяк, Египет', reply_markup=btns6)
        await bot.send_message(call.from_user.id, bem_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, bem1, '2. Мавзолей в Галикарнасе, Турция', reply_markup=btns6)
        await bot.send_message(call.from_user.id, bem1_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, bem2, '3. Колосс Родосский, Греция', reply_markup=btns6)
        await bot.send_message(call.from_user.id, bem2_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, bem3, '4. Храм Артемиды, Эфес, Турция', reply_markup=btns6)
        await bot.send_message(call.from_user.id, bem3_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, bem4, '5. Статуя Зевса, Олимпия, Греция', reply_markup=btns6)
        await bot.send_message(call.from_user.id, bem4_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, bem5, '6. Висячие сады Семирамиды, Азия', reply_markup=btns6)
        await bot.send_message(call.from_user.id, bem5_text)

        time.sleep(2)
        await bot.send_photo(call.from_user.id, bem6, '7. Пирамида Хеопса, Египет', reply_markup=btns6)
        await bot.send_message(call.from_user.id, bem6_text)


    # elif msg == 'chudesa5':




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)