from telebot import types
from loader import bot
from utils.misc.search import history
from database.database_writer import write_in_db

@bot.message_handler(commands=['history'])
def get_history(message: types.Message) -> None:
    bot.send_message(message.from_user.id, f'Последние 10 запросов:\n '
                                           f'{history(message.from_user.id)}')
    write_in_db(message.from_user.full_name, message.from_user.id, message.text)