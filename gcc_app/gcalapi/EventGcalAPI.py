from dataclasses import dataclass
from typing import Optional

from datetime import datetime

from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar


@dataclass
class EventGcalAPI:
    event_id: Optional[str] = None
    summary: Optional[str] = None
    # todo type(start end) ?
    start: Optional[str] = None
    end: Optional[str] = None
    timezone: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    user_id: Optional[int] = None

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
