from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


# Кнопки и клавиатура главного меню
btnWant = InlineKeyboardButton('Хотелка', callback_data='1')

high_lvl_kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(btnWant)

# Кнопки и клавиатура для приложения "Хотелка"
# Верхний уровень
btnName1CheckList = InlineKeyboardButton('В квартиру', callback_data='in_flat')
btnName2CheckList = InlineKeyboardButton('Марине', callback_data='for_Marina')
btnName3CheckList = InlineKeyboardButton('Артёму', callback_data='for_Artem')

Wanty_performance_kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=3).add(
    btnName1CheckList,
    btnName2CheckList,
    btnName3CheckList)

# Нижний уровень
btnAddWanty = InlineKeyboardButton('Добавить хотелку', callback_data='add')
btnRefactor = InlineKeyboardButton('Редактировать', callback_data='refactor')
btnDel = InlineKeyboardButton('Удалить', callback_data='del')

Wanty_ref_kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    btnRefactor,
    btnDel)
