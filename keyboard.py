from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


# Кнопки и клавиатура главного меню
btnWant = InlineKeyboardButton('Хотелка', callback_data='1')

high_lvl_kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(btnWant)

# Кнопки и клавиатура для приложения "Хотелка"
# Верхний уровень
btnCheckList = InlineKeyboardButton('Посмотреть список', callback_data='list')
btnAddWanty = InlineKeyboardButton('Добавить хотелку', callback_data='add')

Wanty_performance_kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    btnCheckList,
    btnAddWanty)

# Нижний уровень
btnRefactor = InlineKeyboardButton('Редактировать', callback_data='refactor')
btnDel = InlineKeyboardButton('Удалить', callback_data='del')

Wanty_ref_kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    btnRefactor,
    btnDel)
