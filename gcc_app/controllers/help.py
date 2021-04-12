from aiogram import types

from gcc_app.app import session, dp
from gcc_app.models import UserModel


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(
        "Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")