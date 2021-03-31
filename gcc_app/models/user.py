from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from gcc_app.config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
#
# engine = create_engine(
#     'postgresql+psycopg2://postgres:1@127.0.0.1:5432/db_gcc', echo=True)


DB = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()

from sqlalchemy import (Column,
                        String,
                        Integer)


# from ..app import DB


class User(DB):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_chat_id = Column(Integer)
    name = Column(String)
    # fullname = Column(String)
    # nickname = Column(String)

    # def __repr__(self):
    #     return "<User(name='%s', fullname='%s', nickname='%s')>" % (
    #         self.name, self.fullname, self.nickname)


create_all = DB.metadata.create_all(engine)
