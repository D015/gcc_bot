from aiogram import types

from gcc_app.access.user import UserAccess
from gcc_app.app import dp


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):

    user_id = UserAccess(telegram_user_id=message.from_user.id,
                         is_bot=message.from_user.is_bot,
                         first_name=message.from_user.first_name,
                         last_name=message.from_user.last_name,
                         username=message.from_user.username,
                         language_code=message.from_user.language_code). \
        create_for_start()

    await message.reply("Привет!\nНапиши мне что-нибудь!")
