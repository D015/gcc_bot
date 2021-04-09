from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional, Union

from gcsa.event import Event
from googleapiclient.errors import HttpError

from gcc_app.app import calendar
from gcc_app.constants import default_summary
from gcc_app.utils import create_default_start


@dataclass
class EventGcalAPI:
    event_id: Optional[str] = None
    summary: Optional[str] = None
    # todo type(start end) - date ?
    start: Union[datetime, date, None] = None
    end: Union[datetime, date, None] = None
    timezone: str = 'UTC'
    description: Optional[str] = None
    location: Optional[str] = None

    def create(self) -> Optional[Event]:
        self.summary = self.summary if self.summary else default_summary

        if type(self.start) is not datetime and type(self.start) is not date:
            self.start = create_default_start()
        # by default, the Google calendar itself creates value from "event_id"
        # in order to set its own value for "event_id", you need to use the "id"
        new_event = Event(id=self.event_id,
                          summary=self.summary,
                          start=self.start,
                          end=self.end,
                          timezone=self.timezone,
                          description=self.description,
                          location=self.location)
        calendar.add_event(new_event)
        event = self.query_by_google_calendar_event_id()
        return event

    def query_by_google_calendar_event_id(self) -> Optional[Event]:
        try:
            event = calendar.get_event(self.event_id)
        except HttpError:
            event = None
        return event
