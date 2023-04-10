import telebot
from telebot import *
import sqlite3

bot = telebot.TeleBot('5995066955:AAFUb9KRCR-b4NeUUmHcgJnHuS2I3IsNxk0')

@bot.message_handler(commands=['db'])
def main(message):
    conn = sqlite3.connect('pickle.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, login varchar(50), tg varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Введите логин')
    bot.register_next_step_handler(message, user_login)

def user_login():
    pass

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    btn_info = types.KeyboardButton('Информация')
    markup.row(btn_info)
    bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['info'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn_site = types.InlineKeyboardButton('Перейти на сайт', url='https://progreenlife.ru/')
    markup.row(btn_site)
    bot.send_message(message.chat.id,
                     'Компания <b>"Green Life"</b> занимается производством и продажей экологически чистых товаров, проведением обучающих семинаров, организацией благотворительных акций, предоставлением консультаций и разработкой инновационных технологий для сохранения окружающей среды. Цель компании - создание более чистой и здоровой среды для жизни и улучшение качества жизни людей.',
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(
    content_types=['video', 'audio', 'photo', 'document', 'sticker', 'video_note', 'voice', 'animation'])
def main(message):
    bot.reply_to(message, 'Бот не воспринимает ничего кроме текста.')


bot.polling(none_stop=True)
