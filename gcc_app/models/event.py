from sqlalchemy import (Column,
                        Boolean,
                        DateTime,
                        String,
                        Integer,
                        ForeignKey)

from gcc_app.models.base import BaseModel


class Event(BaseModel):
    __tablename__ = 'events'

    id = Column(Integer, ForeignKey('base.id'), primary_key=True)

    event_id = Column(String(1024), index=True, unique=True)
    summary = Column(String(56))
    start = Column(DateTime)
    end = Column(DateTime)
    utc_time_offset = Column(String(6))
    timezone = Column(String(50))
    description = Column(String(1024))
    location = Column(String(1024))

    __mapper_args__ = {
        'polymorphic_identity': 'events'
    }

    # def __repr__(self):
    #     return f'User id {self.id} {self.username} chat_id {self.chat_id}'


# print(event.id, ' - ', event.summary, event.start, event.end,
#           event.timezone, event.event_id, event.description, event.location)