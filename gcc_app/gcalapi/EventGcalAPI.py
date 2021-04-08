from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional, Union

from gcsa.event import Event
from googleapiclient.errors import HttpError

from gcc_app.app import calendar
from gcc_app.constants import default_summary, default_start


@dataclass
class EventGcalAPI:
    event_id: Optional[str] = None
    summary: Optional[str] = None
    # todo type(start end) - date ?
    start: Union[datetime, date, None] = None
    end: Union[datetime, date, None] = None
    timezone: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None

    def create(self) -> Optional[Event]:
        self.summary = self.summary if self.summary else default_summary

        if type(self.start) is not datetime and type(self.start) is not date:
            self.start = default_start

        new_event = Event(event_id=self.event_id,
                          summary=self.summary,
                          start=self.start,
                          end=self.end,
                          timezone=self.timezone,
                          description=self.description,
                          location=self.location)
        calendar.add_event(new_event)
        return self.query_by_google_calendar_event_id()

    def query_by_google_calendar_event_id(self) -> Optional[Event]:
        try:
            event = calendar.get_event(self.event_id)
        except HttpError:
            event = None
        return event
