import telebot

token = "token"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types="text")
def hello_world(message):
    bot.send_message(message.chat.id, f"Hello world\nYour id is {message.chat.id}")

bot.polling(none_stop=True)
