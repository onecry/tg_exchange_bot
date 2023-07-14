import os
from dotenv import find_dotenv, load_dotenv
from pathlib import Path

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
RAPID_API_HOST = os.getenv('RAPID_API_HOST')

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR/'database'/'search_history.db'

DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку")
)

CUSTOM_COMMANDS =(
    ('get_list', 'Список валют доступных для конвертации'),
    ('exchange', 'Конвертация валют'),
    ('history', 'Узнать историю запросов'),
)
