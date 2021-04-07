# import datetime
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from sqlalchemy.orm import DeclarativeMeta

from gcc_app.access.base import BaseAccess
from gcc_app.app import session
from gcc_app.models.event import Event


@dataclass
class EventAccess(BaseAccess):
    google_calendar_event_id: Optional[str] = None
    summary: Optional[str] = None
    # todo type(start end) ?
    start: Optional[str] = None
    end: Optional[str] = None
    # todo type(utc_time_offset) ?
    utc_time_offset: Optional[str] = None
    timezone: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    user_id: Optional[int] = None
    __model: Optional[DeclarativeMeta] = Event

    def create(self) -> int:
        new_event = \
            Event(google_calendar_event_id=self.google_calendar_event_id,
                  summary=self.summary,
                  start=self.start,
                  end=self.end,
                  timezone=self.timezone,
                  description=self.description,
                  location=self.location,
                  user_id=self.user_id)
        session.add(new_event)
        session.commit()
        return new_event.id

    def query_by_google_calendar_event_id(self) -> DeclarativeMeta:
        event = session.query(Event).filter_by(
            google_calendar_event_id=self.google_calendar_event_id).first()
        return event
