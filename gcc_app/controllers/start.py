from aiogram import types

from gcc_app.app import session, bot, dp
from gcc_app.models import UserModel


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    print(message)
    new_user = UserModel(chat_id=int(message.from_user.id))
    session.add(new_user)
    session.commit()
    await message.reply("Привет!\nНапиши мне что-нибудь!")