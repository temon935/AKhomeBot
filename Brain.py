import csv


def bot_property():
    return 'Бот по поиску фильмов к твоим услугам!\nМне есть, что предложить тебе на вечер ;)\nНачнем?'


def search():
    pass


def display_wanty():
    pass


def wanty_exists(wanty):
    reader = csv.reader(open("wanty.csv", "rb"), delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        if (row == wanty):
            return True
    return False


def add_wanty(name, phone, address, birthday):
    wanty = [name, phone, address, birthday]
    if wanty_exists(wanty):
        return False

    writer = csv.writer(open("wanty.csv", "ab"), delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(wanty)
    return True


add_wanty('barney', '4321 987', 'New York', '2000')