from aiogram import types

from gcc_app.app import session, bot, dp
from gcc_app.models import User


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    this_user = session.query(User).filter_by(
        telegram_chat_id=int(message.from_user.id)).first()
    # await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")
    await message.reply(this_user.id)