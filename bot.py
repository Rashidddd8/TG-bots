import telebot
from telebot import types
from config import token, admin_tg_ids
import datetime
import db


fio, home, birth, number, comment = '', '', '', '', ''

bot = telebot.TeleBot(token)
word = 0

@bot.message_handler(commands=['start'])
def start(message):
    userIDTG, userNameTG, userFirstNameTG, userLastNameTG = message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Для работы")
    btn2 = types.KeyboardButton("Для учащихся")
    btn3 = types.KeyboardButton("Для ребёнка")
    btn4 = types.KeyboardButton("Для спорта")
    btn5 = types.KeyboardButton("Для отдыха")
    btn6 = types.KeyboardButton("По врачам")
    btn7 = types.KeyboardButton("Из диспансеров")
    btn8 = types.KeyboardButton("Прочие справки")
    btn9 = types.KeyboardButton("Анализы")
    btn10 = types.KeyboardButton("Прививки")
    help_btn = types.KeyboardButton("Поддержка")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, help_btn)
    bot.send_message(message.chat.id,
                     text="В XXI веке разнообразные медицинские заключения занимают важное значение. Их оформление начинается после рождения вплоть до самой смерти. Без справки ты никто! Захотелось в бассейн – предъяви документ. В автошколу, при трудоустройстве – опять требуется резолюция от врача. Купить медицинскую справку можете в нашем центре!".format(
                         message.from_user), reply_markup=markup)
    print(f'userIDTG: {userIDTG}\nuserNameTG: {userNameTG}\nuserFirstNameTG: {userFirstNameTG}\nuserLastNameTG: {userLastNameTG}')
    db.create_user(userIDTG, userNameTG, userFirstNameTG, userLastNameTG)
    db.create_record_btns_table('start', userIDTG, datetime.datetime.now())

@bot.message_handler(commands=['load'])
def load(message):
    if int(message.from_user.id) in admin_tg_ids:
        bot.send_message(message.chat.id,
                             text="".format(
                                 message.from_user))
    else:
        bot.send_message(message.chat.id,
                             text="Сожалеем, но у Вас нет прав на выполнение данной команды :((".format(
                                 message.from_user))


@bot.message_handler(content_types=['text'])
def func(message):
    userIDTG = message.from_user.id
    global word
    if (message.text == "Для работы"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton("086у для работы")
        btn12 = types.KeyboardButton("От нарколога и психиатра")
        btn13 = types.KeyboardButton("Приказ 302н")
        btn14 = types.KeyboardButton("Паспорт здоровья работника")
        btn15 = types.KeyboardButton("Справка на госслужбу")
        btn16 = types.KeyboardButton("989н для гостайны")
        btn17 = types.KeyboardButton("027/у о болезни")
        btn18 = types.KeyboardButton("Для работы форма 405")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, back)
        bot.send_message(message.chat.id, text="Справки для работы", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Поддержка"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Наш менеджер ответит на все Ваши вопросы! Пишите: @Tatarinnnnnnn", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Для учащихся"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn21 = types.KeyboardButton("086у для поступления")
        btn22 = types.KeyboardButton("О временной нетрудоспособности учащихся 095/у")
        btn23 = types.KeyboardButton("Выписка из истории болезни форма 027/у")
        btn24 = types.KeyboardButton("На закрытие пропусков от 14 дней(095/у + 027/у)")
        btn25 = types.KeyboardButton("Справка для академического отпуска")
        btn26 = types.KeyboardButton("Для выхода из академического отпуска")
        btn27 = types.KeyboardButton("Освобождение от физкультуры")
        btn28 = types.KeyboardButton("Справка от врача в свободной форме")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn21, btn22, btn23, btn24, btn25, btn26, btn27, btn28, back)
        bot.send_message(message.chat.id, text="Справки для учащихся", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Для ребёнка"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn31 = types.KeyboardButton("Справка в бассейн")
        btn32 = types.KeyboardButton("Для домашнего обучения")
        btn33 = types.KeyboardButton("Об отсутствии контактов с больными")
        btn34 = types.KeyboardButton("Санаторно-курортная карта для детей 076/у")
        btn35 = types.KeyboardButton("Справка в лагерь форма 079/у")
        btn36 = types.KeyboardButton("Анализ кала - соскоб")
        btn37 = types.KeyboardButton("Карта профилактических прививок 063/у")
        btn38 = types.KeyboardButton("Мед. карта ребёнка 026/у")
        btn39 = types.KeyboardButton("Справка от педиатра")
        btn331 = types.KeyboardButton("Для оформления опеки над ребёнком 164/ - 96")
        btn332 = types.KeyboardButton("Справка реакции Манту")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn31, btn32, btn33, btn34, btn35, btn36, btn37, btn38, btn39, btn331, btn332, back)
        bot.send_message(message.chat.id, text="Справки для ребёнка", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())



    elif (message.text == "Для спорта"):
        # bot.send_message(message.chat.id, text="текст")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn41 = types.KeyboardButton("Справка в бассейн")
        btn42 = types.KeyboardButton("Справка в спортзал")
        btn43 = types.KeyboardButton("Справка для марафона")
        btn44 = types.KeyboardButton("Справка для ГТО")
        btn45 = types.KeyboardButton("Справка для соревнований")
        btn46 = types.KeyboardButton("Справка в спортивную секцию")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn41, btn42, btn43, btn44, btn45, btn46, back)
        bot.send_message(message.chat.id, text="Справки для спорта", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Для отдыха"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn51 = types.KeyboardButton("Санаторно-курортная карта 072/у")
        btn52 = types.KeyboardButton("Справка 070/у для получения путевки")
        btn53 = types.KeyboardButton("Санаторно-курортная карта для детей 076/у")
        btn54 = types.KeyboardButton("Справка 079/у для лагеря")
        btn55 = types.KeyboardButton("Справка 082/у для выезда за границу")
        btn56 = types.KeyboardButton("Сертификат прививок 156/-93")
        btn57 = types.KeyboardButton("Справка в Артек форма 159/у-02")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn51, btn52, btn53, btn54, btn55, btn56, btn57, back)
        bot.send_message(message.chat.id, text="Справки для отдыха", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "По врачам"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn61 = types.KeyboardButton("Справка от терапевта")
        btn62 = types.KeyboardButton("Справка от педиатра")
        btn63 = types.KeyboardButton("Справка от фтизиатра")
        btn64 = types.KeyboardButton("Справка от гинеколога")
        btn65 = types.KeyboardButton("Справка от нарколога")
        btn66 = types.KeyboardButton("Справка от психиатра")
        btn67 = types.KeyboardButton("Справка от стоматолога")
        btn68 = types.KeyboardButton("Справка от невролога")
        btn69 = types.KeyboardButton("Справка от хирурга")
        btn161 = types.KeyboardButton("Справка от гастроэнтеролога")
        btn162 = types.KeyboardButton("Справка от травматолога")
        btn163 = types.KeyboardButton("Справка от лора")
        btn164 = types.KeyboardButton("Справка от психолога")
        btn165 = types.KeyboardButton("Справка от аллерголога")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn61, btn62, btn63, btn64, btn65, btn66, btn67, btn68, btn69, btn161, btn162, btn163, btn164, btn165, back)
        bot.send_message(message.chat.id, text="Справки от докторов", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Из диспансеров"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn71 = types.KeyboardButton("Справка из наркологического диспансера")
        btn72 = types.KeyboardButton("Справка из онкологического диспансера")
        btn73 = types.KeyboardButton("Справка из физкультурного диспансера")
        btn74 = types.KeyboardButton("Справка из психоневрологического диспансера")
        btn75 = types.KeyboardButton("Справка из противотуберкулезного диспансера")
        btn76 = types.KeyboardButton("Справка из кожно-венерологического диспансера")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn71, btn72, btn73, btn74, btn75, btn76, back)
        bot.send_message(message.chat.id, text="Справки из диспансеров", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Прочие справки"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn81 = types.KeyboardButton("Справка в бассейн")
        btn82 = types.KeyboardButton("Справка в Китай")
        btn83 = types.KeyboardButton("Справка ХТИ")
        btn84 = types.KeyboardButton("Справка КЭК")
        btn85 = types.KeyboardButton("Справка о беременности")
        btn86 = types.KeyboardButton("Справка о контактах")
        btn87 = types.KeyboardButton("Справка флюорография")
        btn88 = types.KeyboardButton("Справка о кодировании от алкоголизма")
        btn89 = types.KeyboardButton("Справка из травмпункта")
        btn182 = types.KeyboardButton("Справка донора форма 402/у")
        btn183 = types.KeyboardButton("Направление на госпитализацию форма 057/у-04")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn81, btn82, btn83, btn84, btn85, btn86, btn87, btn88, btn89,  btn182, btn183, back)
        bot.send_message(message.chat.id, text="Прочие справки", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == 'Анализы'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn91 = types.KeyboardButton("Анализ мочи (общий) по форме 210/у")
        btn92 = types.KeyboardButton("Анализ крови – реакция Видаля, по форме 242/у")
        btn93 = types.KeyboardButton("Анализ мочи по Зимницкому по форме 211/у")
        btn94 = types.KeyboardButton("Анализ крови (общий) по форме 224/у")
        btn95 = types.KeyboardButton("Анализ мокроты по форме 216/у")
        btn96 = types.KeyboardButton("Анализ кала (общий) по форме 219/у")
        btn97 = types.KeyboardButton("Анализ кала – яйца глист (гельминтов), скрытая кровь, стеркобилин, билирубин по форме 220/у")
        btn98 = types.KeyboardButton("Анализ кала на кишечную группу")
        btn99 = types.KeyboardButton("Соскоб на энтеробиоз")
        btn191 = types.KeyboardButton("Анализ мочи (Активность альфа-амилазы) по форме 214/у")
        btn192 = types.KeyboardButton("Анализ крови / мочи на наличие в крови алкоголя")
        btn193 = types.KeyboardButton("Анализ крови / мочи на наличие в крови наркотических веществ")
        btn194 = types.KeyboardButton("Биохимический анализ крови 228/у")
        btn195 = types.KeyboardButton("Анализ кала на дисбактериоз")
        btn196 = types.KeyboardButton("Анализ крови на гепатит B, C")
        btn197 = types.KeyboardButton("Анализ (сертификат) на ВИЧ")
        btn198 = types.KeyboardButton("Анализ крови – реакция Вассермана (RW) и др. по форме 241/у")
        btn199 = types.KeyboardButton("Анализ крови / мочи – содержание гормонов и медиаторов по форме 235/у")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn91, btn92, btn93, btn94, btn95, btn96, btn97, btn98, btn99, btn191, btn192, btn193, btn194, btn195, btn196, btn197, btn198, btn199,  back)
        bot.send_message(message.chat.id, text="Анализы", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Прививки"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn201 = types.KeyboardButton("Прививочный сертификат 156/у-93")
        btn202 = types.KeyboardButton("Справка реакция Манту")
        btn203 = types.KeyboardButton("Карта профилактических прививок форма 063/у")
        btn204 = types.KeyboardButton("Справка о прививке от кори")
        btn205 = types.KeyboardButton("Справка о прививке от гепатита")
        btn206 = types.KeyboardButton("Справка о прививке от гриппа")
        btn207 = types.KeyboardButton("Справка о прививке адсм")
        btn208 = types.KeyboardButton("Медотвод от прививок")
        btn209 = types.KeyboardButton("Справка диаскинтест")
        btn210 = types.KeyboardButton("Справка квантифероновый тест")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn201, btn202, btn203, btn204, btn205, btn206, btn207, btn208, btn209, btn210, back)
        bot.send_message(message.chat.id, text="Справки для отдыха", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())



    elif (message.text == "От нарколога и психиатра"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-ot-narkologa-obrazec.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "086у для работы"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-086-y.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        #bot.send_message(message.chat.id, text="Введите ФИО, ваш номер телефона, дату рождения, прописку, место и время доставки", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "От нарколога и психиатра"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-ot-narkologa-obrazec.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Приказ 302н"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kupit-spravku-302n.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())



    elif (message.text == "Паспорт здоровья работника"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-pasport-zdorovya.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1600 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка на госслужбу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kupit-spravku-001-gsu.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "989н для гостайны"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kupit-spravku-989-n.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1500 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "027/у о болезни"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kupit-spravku-027-u.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1500 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Для работы форма 405"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-302-n.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "086у для поступления"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-086-y.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "О временной нетрудоспособности учащихся 095/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-095.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Выписка из истории болезни форма 027/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kupit-spravku-027-u.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1500 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "На закрытие пропусков от 14 дней(095/у + 027/у)"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-095-y.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Справка для академического отпуска"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit akademicheskiy otpusk.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 3000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Для выхода из академического отпуска"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-vihod-iz-akadema.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1600 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Освобождение от физкультуры"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-osvobojdenie-ot-fizkyltyriy.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Справка от врача в свободной форме"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-ot-pediatra.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Справка в бассейн"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-v-basseyn.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 700 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Для домашнего обучения"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Об отсутствии контактов с больными"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kupit-spravku-o-kontaktah.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Санаторно-курортная карта для детей 076/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-076-y.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1500 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Справка в лагерь форма 079/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-079-u.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Анализ кала - соскоб"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-analiz-enterobioz.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Карта профилактических прививок 063/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("karta-profilakticheskih-privivok-obrazec.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1500 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Мед. карта ребёнка 026/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("medicinskaya-karta-rebenka-kypit.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 3500 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Справка от педиатра"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravku-ot-pediatra.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Для оформления опеки над ребёнком 164/ - 96"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-164-y.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 2500 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Справка реакции Манту"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kupit-spravku-mantu-1.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка в бассейн"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-v-basseyn.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 700 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка в спортзал"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-v-sportzal.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 700 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка для марафона"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-dlya-sorevnovanyi.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 700 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка для ГТО"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-dlja-sdachi-norm-gto.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 700 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка для соревнований"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-dlya-sorevnovanyi.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 700 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка в спортивную секцию"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-v-sportivnyu-sekciu.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 700 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Санаторно-курортная карта 072/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("sanatorno-kyrortnaya-karta-072y.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Справка 070/у для получения путевки"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-070-y.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Санаторно-курортная карта для детей 076/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-076-y.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1500 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Справка 079/у для лагеря"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-079-u.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка 082/у для выезда за границу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kupit-spravku-082-u.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Сертификат прививок 156/-93"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("privivochny-sertifikat-obrazec.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 2100 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка в Артек форма 159/у-02"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("privivochny-sertifikat-obrazec.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка от терапевта"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-ot-terapevta.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка от педиатра"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravku-ot-pediatra.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка от фтизиатра"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kupit-spravku-mantu.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка от гинеколога"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-ot-ginekologa.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка от нарколога"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-ot-narkologa-obrazec.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка от психиатра"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-ot-narkologa-obrazec.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка от стоматолога"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-ot-stomatologa.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка от невролога"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-ot-nevrologa.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка от хирурга"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-ot-hiryrga.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка от гастроэнтеролога"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка от травматолога"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-iz-travmpynkta.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка от лора"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-ot-lora.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка от психолога"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-ot-psihologa.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка от аллерголога"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-ot-allergologa.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка из наркологического диспансера"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-iz-narkodispansera.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка из онкологического диспансера"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка из физкультурного диспансера"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-iz-fizkyltyrnogo-dispansera.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка из психоневрологического диспансера"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-iz-psihodispansera-kak-smart-ob'ekt-1.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка из противотуберкулезного диспансера"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка из кожно-венерологического диспансера"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка в бассейн"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-v-basseyn.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 700 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка в Китай"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - от 2500 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Справка ХТИ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-hti.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка КЭК"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-zakluchenie-kek.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - от 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка о беременности"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravku-o-beremennosti.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка о контактах"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kupit-spravku-o-kontaktah.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка флюорография"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-iz-psihodispansera-kak-smart-ob'ekt-1.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка о кодировании от алкоголизма"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-o-kodirovanii.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка из травмпункта"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-iz-travmpynkta.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка донора форма 402/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-donora-kypit.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Направление на госпитализацию форма 057/у-04"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-napravlenie-na-gospitalizaciyu.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Анализ мочи (общий) по форме 210/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-obschii-anliz-mochi.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Анализ крови – реакция Видаля, по форме 242/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 1500 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Анализ мочи по Зимницкому по форме 211/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Анализ крови (общий) по форме 224/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kupit-obschii-analiz-krovi.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Анализ мокроты по форме 216/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Анализ кала (общий) по форме 219/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-obschii-analiz-kala.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Анализ кала – яйца глист (гельминтов), скрытая кровь, стеркобилин, билирубин по форме 220/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Анализ кала на кишечную группу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-analiz-kala-na-kishechnyju-gryppu.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Соскоб на энтеробиоз"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-analiz-enterobioz.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Анализ мочи (Активность альфа-амилазы) по форме 214/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Анализ крови / мочи на наличие в крови алкоголя"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Анализ крови / мочи на наличие в крови наркотических веществ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Биохимический анализ крови 228/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-biohimicheskii-analiz-krovi.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Анализ кала на дисбактериоз"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Анализ крови на гепатит B, C"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-biohimicheskii-analiz-krovi.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Анализ (сертификат) на ВИЧ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-vich.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Анализ крови – реакция Вассермана (RW) и др. по форме 241/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 1200 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Анализ крови / мочи – содержание гормонов и медиаторов по форме 235/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Прививочный сертификат 156/у-93"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("privivochny-sertifikat-obrazec.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 2100 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка реакция Манту"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kupit-spravku-mantu-1.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Карта профилактических прививок форма 063/у"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("karta-profilakticheskih-privivok-obrazec.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1500 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка о прививке от кори"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-kor-kupit.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка о прививке от гепатита"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка о прививке от гриппа"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-privivka-ot-grippa1.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка о прививке адсм"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        bot.send_message(message.chat.id, text="Цена - 800 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Медотвод от прививок"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-medotvod-ot-privivok.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка диаскинтест"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("kypit-spravky-ot-ftiziatra.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    elif (message.text == "Справка квантифероновый тест"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("Оформление справки")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, back)
        p = open("spravka-kvantiferonovie-test.jpg", 'rb')
        bot.send_photo(message.chat.id, p)
        bot.send_message(message.chat.id, text="Цена - 1000 рублей", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Оформление справки"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Оформление заказа. Предоставьте свои данные, следуя инструкциям:", reply_markup=markup)
        bot.send_message(message.chat.id, text="Введите ваше ФИО: \nПример: Иванов Иван Иванович ", reply_markup=markup)
        global word
        word = 1
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())


    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Для работы")
        btn2 = types.KeyboardButton("Для учащихся")
        btn3 = types.KeyboardButton("Для ребёнка")
        btn4 = types.KeyboardButton("Для спорта")
        btn5 = types.KeyboardButton("Для отдыха")
        btn6 = types.KeyboardButton("По врачам")
        btn7 = types.KeyboardButton("Из диспансеров")
        btn8 = types.KeyboardButton("Прочие справки")
        btn9 = types.KeyboardButton("Анализы")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        
        db.create_record_btns_table(message.text, userIDTG, datetime.datetime.now())

    else:
        if word == 1:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(back)
            bot.send_message(message.chat.id, text="Введите дату своего рождения:\nПример: 01.01.2001", reply_markup=markup)
            word = 2
            global fio
            fio = message.text
        elif word == 2:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(back)
            bot.send_message(message.chat.id, text="Введите адрес своей прописки:\nПример: Г. Москва, улица Карла Маркса, дом 58А, Корпус 1, квартира 19", reply_markup=markup)
            word = 3
            global home
            home = message.text
        elif word == 3:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(back)
            bot.send_message(message.chat.id, text="Введите номер своего телефона:\nПример: 8 (999) 555-22-11", reply_markup=markup)
            word = 4
            global birth
            birth = message.text
        elif word == 4:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(back)
            bot.send_message(message.chat.id, text="Комментарий. Место и время доставки\nПример: По месту прописки 20.05 в 20:00", reply_markup=markup)
            word = 5
            global number
            number = message.text
        elif word == 5:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(back)
            bot.send_message(message.chat.id, text="Спасибо за заказ! Данные по заказу отправлены. Ожидайте курьера!", reply_markup=markup)
            word = 6
            global comment
            comment = message.text
            db.create_application(message.from_user.id, fio, home, birth, number, comment)
        else:
            bot.send_message(message.chat.id, text="Я Вас не понимаю :(")


bot.polling(none_stop=True)
