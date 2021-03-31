from sqlalchemy import (Column,
                        Boolean,
                        String,
                        Integer)

from gcc_app.app import DB
from gcc_app.models.base import BaseModel


class UserModel(BaseModel, DB):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, index=True, unique=True)

    is_bot = Column(Boolean)

    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)

    language_code = Column(String)

    def __repr__(self):
        return f'User id {self.id} {self.username} chat_id {self.chat_id}'
