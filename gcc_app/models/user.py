from sqlalchemy import (Column,
                        String,
                        Integer)

from gcc_app.app import DB


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
