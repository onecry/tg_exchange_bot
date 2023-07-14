from telebot import types
from loader import bot
from utils.site_api import list_of_currencies
from database.database_writer import write_in_db

@bot.message_handler(commands=['get_list'])
def send_list(message: types.Message) -> None:
   bot.send_message(message.from_user.id, f'Список валют, доступных для конвертации:\n{list_of_currencies}')
   write_in_db(message.from_user.full_name, message.from_user.id, message.text)