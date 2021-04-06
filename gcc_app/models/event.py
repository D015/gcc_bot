from sqlalchemy import (Column,
                        Boolean,
                        DateTime,
                        String,
                        Integer,
                        ForeignKey)
from sqlalchemy.orm import relationship

from gcc_app.models.base import BaseModel


class Event(BaseModel):
    __tablename__ = 'event'

    id = Column(Integer, ForeignKey('base_model.id'), primary_key=True)

    event_id = Column(String(1024), index=True, unique=True)
    summary = Column(String(56))
    start = Column(DateTime)
    end = Column(DateTime)
    utc_time_offset = Column(String(6))
    timezone = Column(String(50))
    description = Column(String(1024))
    location = Column(String(1024))

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', foreign_keys=[user_id])

    __mapper_args__ = {
        'polymorphic_identity': 'event'
    }

    def __repr__(self):
        return f'Event id {self.id} {self.summary} event_id {self.event_id}'


