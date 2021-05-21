import redis
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import BotCommand
from sqlalchemy import create_engine
# todo from aiopg.sa import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from gcc_app.config import SQLALCHEMY_DATABASE_URI, TOKEN_BOT, REDIS_URI, \
    COMMAND_CREATE_EVENT, COMMAND_HELP, COMMAND_START, COMMAND_TEST

from gcsa.google_calendar import GoogleCalendar

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
DB = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

storage = RedisStorage(**REDIS_URI)

calendar = GoogleCalendar('juniors.py.code.review@gmail.com')

bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command=COMMAND_CREATE_EVENT[0],
                   description=COMMAND_CREATE_EVENT[1]),

        BotCommand(command=COMMAND_HELP[0],
                   description=COMMAND_HELP[1]),

        BotCommand(command=COMMAND_START[0],
                   description=COMMAND_START[1]),

        BotCommand(command=COMMAND_TEST[0],
                   description=COMMAND_TEST[1])
    ]
    await bot.set_my_commands(commands)


async def shutdown(dispatcher: Dispatcher):
    await dp.storage.close()
    await dp.storage.wait_closed()


async def startup(dispatcher: Dispatcher):
    await set_commands(bot)
