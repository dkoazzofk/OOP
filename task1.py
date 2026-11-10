class Book:

    def __init__(self, name, year, words): #конструктор класса
        self.name = name
        self.words = words
        self.year = year
        #print(f'Создание класса Book с названием книги "{name}", и годом издания {year}')

    def __del__(self):
        #pass #если код не нужен в методе класса, то можно просто написать pass
        #print(f'Удалена книга с именем "{self.name}')
        pass

    def __repr__(self):
        return f'Book("{self.name}", {self.words}, {self.year})'


books = [
    Book("Двенадцать стульев", 1928, 110000),
    Book("Тихий Дон", 1940, 380000),
    Book("Преступление и наказание", 1866, 211000),
    Book("Доктор Живаго", 1957, 175000),
    Book("Мастер и Маргарита", 1967, 120000),
    Book("Евгений Онегин", 1833, 23000),
    Book("1984", 1949, 89000),
    Book("Гарри Поттер и философский камень", 1997, 77000),
    Book("Отцы и дети", 1862, 65000),
    Book("Мёртвые души", 1842, 130000),
    Book("Собачье сердце", 1925, 30000),
    Book("Война и мир", 1869, 587000),
]

def sort_book_words(books):
    print(f'Неотсортированный список книг: \n{books}')
    lenght = len(books)
    for i in range(lenght):
        for j in range(0, lenght - i - 1):
            if books[j].words < books[j + 1].words:
                books[j], books[j + 1] = books[j + 1], books[j]
    print(f'Отсортированный список книг: \n{books}')


sort_book_words(books)