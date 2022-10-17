import telebot

class Book:
    'Параметры книги на голосование'

    def __init__(self, bot):
        self.author = ''
        self.bookName = ''
        self.numOfPages = 0
        self.anotation = ''
        self.description = ''
        self.genre = ''
        self.bot = bot

    def setAuthor(self, author):
        self.author = author

    def setBookName(self, bookName):
        self.bookName = bookName

    def setNumOfPages(self, numOfPages):
        self.numOfPages = numOfPages

    def setAnotation(self, anotation):
        self.anotation = anotation

    def setDescription(self, description):
        self.description = description

    def setGenre(self, genre):
        self.genre = genre

    def itog(self, message, golos):
        self.bot.send_message(message.from_user.id, 'Сейчас записано:\n' + 'Голосование: #' + str(
            golos) + 'я\n' + '1)Автор: ' + self.author + '\n2)Название книги: ' + self.bookName + '\n3)Жанр книги: ' + self.genre + '\n4)Количество страниц: ' + str(
            self.numOfPages) + '\n5)Ссылка на описание: ' + self.description + '\n6)Анотация: ' + self.anotation + '\n\nВсё верно?')
