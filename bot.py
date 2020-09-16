# import telebot
#
# bot = telebot.TeleBot('1344039009:AAFD6_y_lejW8Xc4LflBxP-U24dXr--JpbE')
#
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Привет,спасибо что запустил меня',reply_markup=kp)
#
# kp = telebot.types.ReplyKeyboardMarkup()
# kp.row('Hi', 'Bye')
# @bot.message_handler(content_types=['text'])
# def sending_text(message):
#     if message.text == 'Привет':
#         bot.send_message(message.chat.id,'Привет человек')
#     elif message.text == 'Как дела робот?':
#         bot.send_message(message.chat.id, 'У робота дела идут хорошо')
#     elif message.text == 'Боты захватят мир?':
#         bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAIEM19DQbIPXi6NBh-eh2TMghD4khVJAAJaBQAC6VUFGK3ZOkeA0hgDGwQ')
#     elif message.text == 'Ты красотка?':
#         bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAIEPV9DQozZoVvFE3GZIIki0OLVR00HAAJPBQAC6VUFGEtnrZK8eUl8GwQ')
#     elif message.text == 'Пока':
#         bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIER19DSTtnhqjNO3s7NNaL9q9F2UEOAAJuBQAC6VUFGB_He7D1MMdlGwQ')
# bot.polling()

import telebot

bot = telebot.TeleBot('1344039009:AAFD6_y_lejW8Xc4LflBxP-U24dXr--JpbE')

# keyboard1 = telebot.types.ReplyKeyboardMarkup()
# keyboard1.row('Привет', 'Пока')
kp = telebot.types.ReplyKeyboardMarkup()
kp.row('Привет', 'Как дела робот?', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет,спасибо что запустил меня',reply_markup=kp)

@bot.message_handler(content_types=['text'])
def sending_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет человек')
    elif message.text == 'Как дела робот?':
        bot.send_message(message.chat.id, 'У робота дела идут хорошо')
    elif message.text == 'Боты захватят мир?':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIDFV8_wMJ--2k7VjLIWOWB5Q12ne4xAAKBEQACPLPFB0bAzHDYX3P9GwQ')
    elif message.text == 'Пока':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIEQ19DSNQJWWAjPKbba6MIHb-X9qZ0AALsAAPww8AOm5n8Nu56jzwbBA')


#CAACAgIAAxkBAAIEQ19DSNQJWWAjPKbba6MIHb-X9qZ0AALsAAPww8AOm5n8Nu56jzwbBA


bot.polling()