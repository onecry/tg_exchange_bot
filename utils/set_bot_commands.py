from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS, CUSTOM_COMMANDS

def set_custom_commands(bot):
    bot.set_my_commands([BotCommand(*i_com) for i_com in CUSTOM_COMMANDS])

def set_default_commands(bot):
    bot.set_my_commands([BotCommand(*i_com) for i_com in DEFAULT_COMMANDS])
