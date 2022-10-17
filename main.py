import telebot
from telebot import types
from book import Book

bot = telebot.TeleBot('5760407234:AAFuJAKQPlq1nSgS028nzi6MSojBppqCkTY')
golos = 0

prov = False

n1 = Book(bot)

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "В какое голосование добавляем?")
        bot.register_next_step_handler(message, num_golos)
    elif message.text == '/book':
        n1.itog(message, golos)
    else:
        bot.send_message(message.from_user.id, "Напиши /reg")


def num_golos(message):
    global golos, prov
    prov = False
    golos = 0
    try:
        golos = int(message.text)
        prov = (golos != 0)
    except Exception:
        bot.send_message(message.from_user.id, "Цифрами вводи")
    if prov and (golos > 0):
        bot.send_message(message.from_user.id, "Укажи автора")
        bot.register_next_step_handler(message, get_author)
    else:
        bot.send_message(message.from_user.id, 'Некореектное значение, попробуй ещё раз')
        bot.register_next_step_handler(message, num_golos)


def get_author(message):
    n1.setAuthor(message.text)
    bot.send_message(message.from_user.id, 'Какое название у книги?')
    bot.register_next_step_handler(message, get_book);


def get_book(message):
    n1.setBookName(message.text)
    bot.send_message(message.from_user.id, 'Какой жанр у твоей книги?')
    bot.register_next_step_handler(message, get_genre)


def get_genre(message):
    n1.setGenre(message.text)
    bot.send_message(message.from_user.id, 'Сколько в ней страниц?')
    bot.register_next_step_handler(message, get_pages)


def get_pages(message):
    global prov
    prov = False
    n1.setNumOfPages(0)
    try:
        n1.setNumOfPages(message.text)
        prov = (n1.numOfPages != 0)
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    if prov and (int(n1.numOfPages) > 0):
        bot.send_message(message.from_user.id, 'А теперь дай ссылку на описание')
        bot.register_next_step_handler(message, get_description)
    else:
        bot.send_message(message.from_user.id, 'Некореектное значение, попробуй ещё раз')
        bot.register_next_step_handler(message, get_pages)


def get_description(message):
    n1.setDescription(message.text)
    bot.send_message(message.from_user.id, 'Введи краткую анотацию')
    bot.register_next_step_handler(message, get_anotation)


def get_anotation(message):
    n1.setAnotation(message.text)
    n1.itog(message)
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    bot.send_message(message.from_user.id, text='Всё верно?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.from_user.id, "Значит отправляем")
    elif call.data == "no":
        bot.send_message(call.from_user.id, "Давайте исправим")
        bot.send_message(call.from_user.id, "Напиши /reg")
    else:
        bot.send_message(call.from_user.id, "Я вас не понял")
        bot.register_next_step_handler(call, get_conf)


def get_conf(message):
    if (message.text == 'Да') or (message.text == 'да'):
        bot.send_message(message.from_user.id, "Значит отправляем")
    elif (message.text == 'Нет') or (message.text == 'нет'):
        bot.send_message(message.from_user.id, "Давайте исправим")
        bot.send_message(message.from_user.id, "В какое голосование добавляем?")
        bot.register_next_step_handler(message, num_golos)
    else:
        bot.send_message(message.from_user.id, "Я вас не понял")
        bot.register_next_step_handler(message, get_conf)


bot.polling(none_stop=True, interval=0)
