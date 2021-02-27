from email.mime import message

import telebot
import keyboards
import random

bot = telebot.TeleBot('1670660949:AAEHYPAHmgzpGVKDU73gu0myl4JZ9Ni3i8U')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Приветствую вас с вами игровой бот по математике!!!', reply_markup=keyboards.menu_btn)


@bot.message_handler(content_types=['text'])
def math(message):
    if message.text == 'Играть':
        a = random.randint(1,10)
        b = random.randint(1,20)
        result = str(a + b)
        bot.send_message(message.chat.id, a)
        bot.send_message(message.chat.id, f'result: {result}')





 #   a = random.randit(1,10)
 #   b = random.randit(1,20)

bot.polling()



# 1. a = 1 int
# 2. b = c 1.2 float
# 3. c = True # Bool/False
# 4. list = ['Text'