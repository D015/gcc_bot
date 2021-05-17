import redis
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from sqlalchemy import create_engine
# todo from aiopg.sa import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from gcc_app.config import SQLALCHEMY_DATABASE_URI, TOKEN_BOT, REDIS_URI

from gcsa.google_calendar import GoogleCalendar

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
DB = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
redis_db = redis.Redis(**REDIS_URI)

bot = Bot(token=TOKEN_BOT)
# dp = Dispatcher(bot)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

calendar = GoogleCalendar('juniors.py.code.review@gmail.com')




async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()
