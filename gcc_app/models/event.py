from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.dialects.postgresql import UUID

from gcc_app.app import db
from gcc_app.global_utils import create_uuid4_hex
from gcc_app.models.base import BaseModel


class EventModel(BaseModel, db):
    __tablename__ = "event"

    # todo move default=create_uuid4 into def __init__
    google_calendar_event_id = Column(
        String(32), unique=True, default=create_uuid4_hex
    )
    summary = Column(String(56))
    start = Column(DateTime)
    end = Column(DateTime)
    # todo type(utc_time_offset) ?
    utc_time_offset = Column(String(6))
    timezone = Column(String(50))
    conference_link = Column(String(2000))
    document_link = Column(String(2000))
    description = Column(String(1024))
    location = Column(String(2000))
    user_id = Column(Integer, ForeignKey("user.id"))
    # todo select the type of cascade deletion ?
    user = relationship(
        "UserModel",
        foreign_keys=[user_id],
        # cascade="all, delete",
        backref=backref("events", lazy="noload"),
    )

    __mapper_args__ = {"eager_defaults": True}

    def __repr__(self):
        return f"Event id {self.id} {self.summary} event_id {self.google_calendar_event_id}"
