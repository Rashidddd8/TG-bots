import telebot
from telebot import types  # для указание типов
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("Наш сайт")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, ".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Банкротство граждан и организаций")
        btn2 = types.KeyboardButton("Налоговое право")
        btn3 = types.KeyboardButton("ДТП")
        btn4 = types.KeyboardButton("Уголовное право")
        btn5 = types.KeyboardButton("Защита прав потребителей")
        btn6 = types.KeyboardButton("Арбитражные споры")
        btn7 = types.KeyboardButton("Товароведческая экспертиза")
        btn8 = types.KeyboardButton("Споры со страховыми компаниями")
        btn9 = types.KeyboardButton("Семейные споры")
        btn10 = types.KeyboardButton("Жилищные споры")
        btn11 = types.KeyboardButton("Наследственные споры")
        btn12 = types.KeyboardButton("Защита прав собственника")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)


    elif message.text == "Банкротство граждан и организаций":
        p = open("банкротство.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Получите онлайн консультацию на нашем сайт pravdakon.ru совершенно бесплатно!")

    elif message.text == "Налоговое право":
        p = open("Налоги.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Получите онлайн консультацию на нашем сайт pravdakon.ru совершенно бесплатно!")

    elif message.text == "ДТП":
        p = open('Дтп.jpg', 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Получите онлайн консультацию на нашем сайт pravdakon.ru совершенно бесплатно!")

    elif message.text == "Уголовное право":
        p = open('Уголовное.jpg', 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Получите онлайн консультацию на нашем сайт pravdakon.ru совершенно бесплатно!")

    elif message.text == "Защита прав потребителей":
        p = open('Потребитель.jpg', 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Получите онлайн консультацию на нашем сайт pravdakon.ru совершенно бесплатно!")

    elif message.text == "Арбитражные споры":
        p = open('Арбитражные.jpg', 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Получите онлайн консультацию на нашем сайт pravdakon.ru совершенно бесплатно!")

    elif message.text == "Товароведческая экспертиза":
        p = open('Товарка.jpg', 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Получите онлайн консультацию на нашем сайт pravdakon.ru совершенно бесплатно!")

    elif message.text == "Споры со страховыми компаниями":
        p = open('Споры.jpg', 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Получите онлайн консультацию на нашем сайт pravdakon.ru совершенно бесплатно!")

    elif message.text == "Семейные споры":
        p = open('Семейные.jpg', 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Получите онлайн консультацию на нашем сайт pravdakon.ru совершенно бесплатно!")

    elif message.text == "Жилищные споры":
        p = open('Жилищные.jpg', 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Получите онлайн консультацию на нашем сайт pravdakon.ru совершенно бесплатно!")

    elif message.text == "Наследственные споры":
        p = open('Наследство.jpg', 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Получите онлайн консультацию на нашем сайт pravdakon.ru совершенно бесплатно!")

    elif message.text == "Защита прав собственника":
        p = open('Защита.jpg', 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Получите онлайн консультацию на нашем сайт pravdakon.ru совершенно бесплатно!")




    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("Наш сайт")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif (message.text == "Наш сайт"):
        bot.send_message(message.chat.id, text="https://pravdakon.ru/")

    else:
        bot.send_message(message.chat.id, text="На такую команду я не запрограммировал..")


bot.polling(none_stop=True)
