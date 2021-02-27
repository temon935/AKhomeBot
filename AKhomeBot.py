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
    if callback_query.data == '1':
        await bot.send_message(callback_query.from_user.id, 'Меню "Хотелки"', reply_markup=kb.Wanty_performance_kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)