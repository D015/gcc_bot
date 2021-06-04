from aiogram.contrib.fsm_storage.redis import RedisStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import BotCommand

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from gcc_app.config import (
    SQLALCHEMY_DATABASE_URI,
    TOKEN_BOT,
    REDIS_URI,
    COMMAND_CREATE_EVENT,
    COMMAND_HELP,
    COMMAND_START,
    COMMAND_TEST, EMAIL_GOOGLE_CALENDAR,
)


from gcsa.google_calendar import GoogleCalendar

DB = declarative_base()


async def create_async_session():
    engine = create_async_engine(SQLALCHEMY_DATABASE_URI, echo=True)
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    return async_session()


storage = RedisStorage(**REDIS_URI)

calendar = GoogleCalendar(EMAIL_GOOGLE_CALENDAR)

bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command=COMMAND_CREATE_EVENT[0], description=COMMAND_CREATE_EVENT[1]
        ),
        BotCommand(command=COMMAND_HELP[0], description=COMMAND_HELP[1]),
        BotCommand(command=COMMAND_START[0], description=COMMAND_START[1]),
        BotCommand(command=COMMAND_TEST[0], description=COMMAND_TEST[1]),
    ]
    await bot.set_my_commands(commands)


async def shutdown(dispatcher: Dispatcher):
    await dp.storage.close()
    await dp.storage.wait_closed()


async def startup(dispatcher: Dispatcher):
    await set_commands(bot)
