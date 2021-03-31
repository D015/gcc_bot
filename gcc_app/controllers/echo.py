from aiogram import types

from gcc_app.app import bot, dp



@dp.message_handler()
async def echo_message(message: types.Message):
    print(message.from_user.id)
    print(message)
    await bot.send_message(message.from_user.id, message.text)