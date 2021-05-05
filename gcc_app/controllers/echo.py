from aiogram import types

from gcc_app.app import bot, dp



@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)