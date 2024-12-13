class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        print('Название книги: ' + self.title + '. Автор: ' + self.author + '. Год издания: '+ str(self.year) + '.')

book1 = Book('Колобок', 'Народ', 1234)

book1.get_info()