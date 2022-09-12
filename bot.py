import config
import telebot
from telebot import types # для указание типов

from hh_parsing import parse_data
from handel_data import handel_vacancies
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def strat_bot(message):
    bot.send_message(message.chat.id, 'Бот готов к поиску вакансий', reply_markup=check_button)


@bot.message_handler(regexp='Проверить')
def get_vacancy(message):
    raw_data = parse_data()
    data = handel_vacancies(raw_data)
    if not data:
        bot.send_message(message.chat.id, 'новых вакансий нет..')
    else:
        for text in data:
            bot.send_message(message.chat.id, text, parse_mode='html')


@bot.message_handler()
def another_answer(message):
    bot.send_message(message.chat.id, 'Не понимаю.. Нажмите кнопку Проверить!', reply_markup=check_button)


if __name__ == '__main__':
     bot.infinity_polling()