from telebot.handler_backends import State, StatesGroup

class UserState(StatesGroup):
    from_value = State()
    to_value = State()