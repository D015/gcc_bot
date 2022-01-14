from datetime import datetime, date
from typing import Optional, Union

from gcsa.event import Event
from googleapiclient.errors import HttpError

from app import calendar
from constants import DEFAULT_SUMMARY
from utils import create_default_start


class EventGcalAPI:
    @classmethod
    def create(
        cls,
        event_id: Optional[str] = None,
        summary: Optional[str] = None,
        start: Union[datetime, date, None] = None,
        description: Optional[str] = None,
        location: Optional[str] = None,
    ) -> Optional[Event]:
        summary = summary if summary else DEFAULT_SUMMARY
        if type(start) is not datetime and type(start) is not date:
            start = create_default_start()
        # by default, the Google calendar itself creates value from "event_id"
        # in order to set its own value for "event_id", you need to use the "id"
        new_event = Event(
            id=event_id,
            summary=summary,
            start=start,
            description=description,
            location=location,
        )
        calendar.add_event(new_event)
        event = cls.query_by_google_calendar_event_id(event_id=event_id)
        return event

    @staticmethod
    def query_by_google_calendar_event_id(
        event_id,
    ) -> Union[Event, bool, None]:
        try:
            event = calendar.get_event(event_id)
        except HttpError:
            event = False
        return event
