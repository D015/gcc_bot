from aiogram import types

from gcc_app.access.user import UserAccess
from gcc_app.app import session, dp


@dp.message_handler(commands=['test'])
async def process_test_command(message: types.Message):
    print(message)
    UserAccess(chat_id=message.from_user.id).create_user()

    await message.reply("Привет!\nНапиши мне что-нибудь!")