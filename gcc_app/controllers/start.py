from aiogram import types

from access.user import UserAccess
from app import dp


@dp.message_handler(state="*", commands=["start"])
async def process_start_command(message: types.Message):
    await UserAccess.create_for_start(
        telegram_user_id=message.from_user.id,
        is_bot=message.from_user.is_bot,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        username=message.from_user.username,
        language_code=message.from_user.language_code,
    )
    await message.reply("Привет!\nНапиши мне что-нибудь!")
