import telebot

from config import TOKEN
from handlers.handlers import register_handlers


bot = telebot.TeleBot(TOKEN)


register_handlers(bot)


print("LINK Bot Started...")


bot.infinity_polling(skip_pending=True)