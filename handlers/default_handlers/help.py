from telebot import types
from loader import bot
from config_data.config import CUSTOM_COMMANDS
from database.database_writer import write_in_db



@bot.message_handler(commands=['help'])
def send_list(message: types.Message) -> None:
   bot.send_message(message.from_user.id, f'Команды бота:\n{CUSTOM_COMMANDS[0]}\n{CUSTOM_COMMANDS[1]}\n'
                                          f'{CUSTOM_COMMANDS[2]}')
   write_in_db(message.from_user.full_name, message.from_user.id, message.text)
