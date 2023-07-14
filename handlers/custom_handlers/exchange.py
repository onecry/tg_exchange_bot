from telebot.types import Message
from loader import bot
from states.states_info import UserState
from keyboards.inline.currency_markup import currency_markup
from utils.site_api import list_of_currencies, get_exchanged_value
from database.database_writer import write_in_db

@bot.message_handler(commands='exchange')
def exchange(message: Message) -> None:
    bot.set_state(message.from_user.id, UserState.from_value, message.chat.id)
    bot.send_message(message.from_user.id, f'Выберете валюту, курс которой хотите узнать',
                     reply_markup=currency_markup())
    write_in_db(message.from_user.full_name, message.from_user.id, message.text)

@bot.message_handler(state=UserState.from_value)
def get_from_value(message: Message) -> None:
    if message.text in list_of_currencies:
        bot.send_message(message.from_user.id, f'Теперь выберете валюту, что бы узнать курс относительно {message.text}',
                            reply_markup=currency_markup())
        bot.set_state(message.from_user.id, UserState.to_value, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                data['from'] = message.text
    else:
        bot.send_message(message.from_user.id, 'Выбирайте из предложенных вариантов', reply_markup=currency_markup())

@bot.message_handler(state=UserState.to_value)
def get_to_value(message: Message) -> None:
    if message.text in list_of_currencies:
        bot.send_message(message.from_user.id, 'Выполняется конвертация')

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                data['to'] = message.text

                qrstr = {"from": f"{data['from']}", "to": f"{data['to']}", "q": "1.0"}

                exchanged_value = get_exchanged_value(qrstr)

                bot.send_message(message.from_user.id, exchanged_value)

        bot.delete_state(message.from_user.id, message.chat.id)
    else:
        bot.send_message(message.from_user.id, 'Выбирайте из предложенных вариантов', reply_markup=currency_markup())