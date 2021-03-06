import Brain
import config
import logging
import asyncio
import keyboard as kb
from aiogram import Bot, Dispatcher, executor, types


# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def any_msg(message: types.Message):
    await bot.send_message(message.chat.id, "Главное меню", reply_markup=kb.high_lvl_kb)


@dp.callback_query_handler(lambda c: c.data == '1')
async def callback_btn1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите принадлежность "хотелки"', reply_markup=kb.Wanty_performance_kb)


@dp.callback_query_handler(lambda c: c.data == 'in_flat' or 'for_Marina' or 'for_Artem')
async def callback_btn1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await show(callback_query.from_user.id, callback_query.data)


async def show(callback_query, data):
    if data == 'for_Marina':
        answer = Brain.display_wanty_Marina()
        for i in answer:
            await bot.send_message(callback_query, i)    # , reply_markup=kb.Wanty_ref_kb)
    elif data == 'for_Artem':
        answer = Brain.display_wanty_Artem()
        for i in answer:
            await bot.send_message(callback_query, i)    # , reply_markup=kb.Wanty_ref_kb)
    elif data == 'in_flat':
        answer = Brain.display_wanty_flat()
        for i in answer:
            await bot.send_message(callback_query, i)    # , reply_markup=kb.Wanty_ref_kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)