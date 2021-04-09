# import datetime
from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional, Union

from sqlalchemy.orm import DeclarativeMeta

from gcc_app.access.base import BaseAccess
from gcc_app.app import session
from gcc_app.constants import default_summary
from gcc_app.models.event import EventModel
from gcc_app.utils import create_default_start


@dataclass
class EventAccess(BaseAccess):
    google_calendar_event_id: Optional[str] = None
    summary: Optional[str] = None
    # todo type(start end) - date ?
    start: Union[datetime, date, None] = None
    end: Union[datetime, date, None] = None
    # todo type(utc_time_offset) ?
    utc_time_offset: Optional[str] = None
    timezone: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    user_id: Optional[int] = None
    __model: Optional[DeclarativeMeta] = EventModel

    def create(self) -> EventModel:
        self.summary = self.summary if self.summary else default_summary

        if type(self.start) is not datetime and type(self.start) is not date:
            self.start = create_default_start()

        new_event = \
            EventModel(google_calendar_event_id=self.google_calendar_event_id,
                       summary=self.summary,
                       start=self.start,
                       end=self.end,
                       timezone=self.timezone,
                       description=self.description,
                       location=self.location,
                       user_id=self.user_id)
        session.add(new_event)
        session.commit()
        return new_event

    def query_by_google_calendar_event_id(self) -> DeclarativeMeta:
        event = session.query(EventModel).filter_by(
            google_calendar_event_id=self.google_calendar_event_id).first()
        return event
