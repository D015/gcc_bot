from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import Config

from models import User, session, create_all


bot = Bot(token=Config.TOKEN_BOT)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    print(message.from_user.id)
    new_user = User(telegram_chat_id=int(message.from_user.id))
    session.add(new_user)
    session.commit()
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    this_user = session.query(User).filter_by(
        telegram_chat_id=int(message.from_user.id)).first()
    # await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")
    await message.reply(this_user.id)


@dp.message_handler()
async def echo_message(message: types.Message):
    print(message.from_user.id)
    print(message)
    await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
    create_all