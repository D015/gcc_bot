from sqlalchemy import (Column,
                        Boolean,
                        String,
                        Integer,
                        ForeignKey)
from sqlalchemy.orm import relationship, backref

from gcc_app.models.base import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    id = Column(Integer, ForeignKey('base_model.id'), primary_key=True)

    chat_id = Column(Integer, index=True, unique=True)
    is_bot = Column(Boolean)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50))
    language_code = Column(String(6))

    # todo select the type of cascade deletion ?
    # todo lazy configuration
    # events = relationship('Event', foreign_keys=[id], cascade='all,delete',
    #                       backref='user')
    events = relationship('Event', foreign_keys=[id])

    __mapper_args__ = {
        'polymorphic_identity': 'user'
    }

    def __repr__(self):
        return f'User id {self.id} {self.username} chat_id {self.chat_id}'
