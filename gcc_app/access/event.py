from datetime import datetime, date
from typing import Optional, Union

from sqlalchemy.future import select

from gcc_app.access.base import BaseAccess
from gcc_app.app import create_async_session
from gcc_app.constants import DEFAULT_SUMMARY
from gcc_app.global_utils import create_uuid4_hex
from gcc_app.models import EventModel

from gcc_app.utils import create_default_start


class EventAccess(BaseAccess):
    @staticmethod
    async def create(
        google_calendar_event_id: Optional[str] = None,
        summary: Optional[str] = None,
        # todo type(start end) - date ?
        start: Union[datetime, date, None] = None,
        end: Union[datetime, date, None] = None,
        # todo type(utc_time_offset) ?
        utc_time_offset: Optional[str] = None,
        timezone: Optional[str] = None,
        conference_link: Optional[str] = None,
        document_link: Optional[str] = None,
        description: Optional[str] = None,
        location: Optional[str] = None,
        user_id: Optional[int] = None,
    ) -> EventModel:
        summary = summary if summary else DEFAULT_SUMMARY

        if type(start) is not datetime and type(start) is not date:
            start = create_default_start()
        # if google_calendar_event_id is None:
        #     # TODO Use create_uuid4_hex in Access or in Model?
        #     google_calendar_event_id = create_uuid4_hex()

        async with await create_async_session() as session:
            async with session.begin():
                new_event = EventModel(
                    # google_calendar_event_id=google_calendar_event_id,
                    summary=summary,
                    start=start,
                    end=end,
                    timezone=timezone,
                    conference_link=conference_link,
                    document_link=document_link,
                    description=description,
                    location=location,
                    user_id=user_id,
                )
                session.add(new_event)
        return new_event

    @staticmethod
    async def query_by_google_calendar_event_id(
        google_calendar_event_id: Optional[str] = None,
    ) -> EventModel:
        async with await create_async_session() as session:
            events = await session.execute(
                select(EventModel).filter_by(
                    google_calendar_event_id=google_calendar_event_id
                )
            )
            event = events.scalars().first()
        return event
