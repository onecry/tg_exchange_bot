from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from utils.site_api import list_of_currencies

def currency_markup() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True, one_time_keyboard=True)
    for i_elem in list_of_currencies:
        markup.add(KeyboardButton(i_elem))

    return markup