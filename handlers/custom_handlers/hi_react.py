from telebot import types
from loader import bot
from database.database_writer import write_in_db

@bot.message_handler(content_types='text')
def hi_react(message: types.Message) -> None:
    if message.text=='Привет':
       bot.reply_to(message, f'Привет! {message.from_user.full_name}')
       write_in_db(message.from_user.full_name, message.from_user.id, message.text)

    else:
        bot.reply_to(message, f'Бот не поддерживает данную команду\n'
                              f'Введите /help для получения информации о командах бота')
        write_in_db(message.from_user.full_name, message.from_user.id, message.text)