import config
import telebot
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_type=('text'))
def foo(message):
    bot.send_message(message.chat.id, 'hello')

if __name__ == '__main__':
    bot.infinity_polling()