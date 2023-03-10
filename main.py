from dotenv import load_dotenv
# carga las variables del archivo .env
load_dotenv()

import telebot
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def send_welcome(message):
	print("message : ",message)
	bot.reply_to(message, "Hola este es un mensaje ed prueba")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	print("message : ",message)
	bot.reply_to(message, "HELP")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()