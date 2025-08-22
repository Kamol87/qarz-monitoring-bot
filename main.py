import os
import telebot

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, Виктор! Сигналы будут приходить сюда.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, f"Получено: {message.text}")

bot.polling()
