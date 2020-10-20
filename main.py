import telebot
from telebot import types

atoken = '1227648472:AAH2nPNdMFNfSnYMdJGN6sw51tUE6iogU9I'
bot = telebot.TeleBot(atoken)

print("Start bot...")

name = ' '
surname = ' '
age = 0

@bot.message_handler(content_types=['sticker'])
def hello(message):
    bot.send_message(message.from_user.id, 'Отправь стикер')
    print(message)
    bot.register_next_step_handler(message, get_otvet)

def get_otvet(message):
    bot.send_message(message, 'Спасибо')

@bot.message_handler(content_types=['text'])

def poka(message):
    if message.text == 'пока':
        bot.send_message(message.from_user, 'Прощай')
        bot.send_sticker(message.chat_id, 'CAACAgIAAxkBAAPOX3xm683Nw6JS8MzMudjXx3WEcXYAAuEAA1KJkSM5wTa2R1-UzBsE')


def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'Как тебя зовут?')
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Напиши свой возраст')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    age = int(message.text)

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text= 'Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе ' + str(age) + ' лет. Тебя зовут ' + name + ' ' + surname +'. Все верно?'
    bot.send_message(message.from_user.id, text=question, reply_markup= keyboard)



@bot.callback_query_handler(func= lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Окей, запомню;)')
        bot.send_sticker(call.message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Напиши /reg и пройди регистрацию заново;)')
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAOdX3xlFpuGlBRDCEznI1Ut8pHKMq8AAlYJAAJ5XOIJ0j_fLLsb5eQbBA')

bot.polling(none_stop=True, interval= 0)