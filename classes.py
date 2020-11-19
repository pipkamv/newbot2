from aiogram.dispatcher.filters.state import State, StatesGroup

class Users(list):
    cart = []

    def __init__(self, cart):
        self.cart = cart

    def __str__(self):
        return f'Корзина: {self.cart}'

class Form(StatesGroup):
    starting = State()
    first_step = State()
    second_step = State()
    dambl_step = State()

