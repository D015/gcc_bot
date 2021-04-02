from aiogram import types

from gcc_app.access.user import UserAccess
from gcc_app.app import session, dp
from gcc_app.models import User


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    print(message)

    user_id = UserAccess(chat_id=message.from_user.id,
                         is_bot=message.from_user.is_bot,
                         first_name=message.from_user.first_name,
                         last_name=message.from_user.last_name,
                         username=message.from_user.username,
                         language_code=message.from_user.language_code). \
        create_user_for_start()

    print(user_id)

    await message.reply("Привет!\nНапиши мне что-нибудь!")
