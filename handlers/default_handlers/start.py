from telebot import types
from loader import bot
from database.database_writer import write_in_db
from database.storage import db, User

tables = [User]
if not all(i.table_exists() for i in tables):
    db.create_tables(tables)

@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message) -> None:
   bot.send_message(message.from_user.id, f'Привет! {message.from_user.full_name}')
   write_in_db(message.from_user.full_name, message.from_user.id, message.text)