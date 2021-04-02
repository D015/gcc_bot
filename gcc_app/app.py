from sqlalchemy import create_engine
# todo from aiopg.sa import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from gcc_app.config import SQLALCHEMY_DATABASE_URI, TOKEN_BOT

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
DB = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot)