from sqlalchemy import (Column,
                        DateTime,
                        String,
                        Integer,
                        ForeignKey)
from sqlalchemy.orm import relationship, backref

from gcc_app.models.base import BaseModel


class EventModel(BaseModel):
    __tablename__ = 'event'

    id = Column(Integer, ForeignKey('base_model.id'), primary_key=True)
    # todo move default=create_uuid4 into def __init__
    google_calendar_event_id = Column(String(1024), index=True, unique=True)
    summary = Column(String(56))
    # todo decide whether to make a default
    #  in the model (start=create_default_start)  or not
    start = Column(DateTime)
    end = Column(DateTime)
    # todo type(utc_time_offset) ?
    utc_time_offset = Column(String(6))
    timezone = Column(String(50))
    conference_link = Column(String(2000))
    document_link = Column(String(2000))
    description = Column(String(1024))
    location = Column(String(2000))
    user_id = Column(Integer, ForeignKey('user.id'))
    # todo select the type of cascade deletion ?
    user = relationship(
        'UserModel', foreign_keys=[user_id], cascade='all, delete',
        backref=backref('events', lazy='dynamic'))

    __mapper_args__ = {
        'polymorphic_identity': 'event'
    }

    def __repr__(self):
        return f'Event id {self.id} {self.summary} event_id {self.google_calendar_event_id}'


