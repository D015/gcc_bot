from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from access import EventAccess
from access import UserAccess
from app import dp
from constants import DATE, TIME, HOUR, MINUTE, CONFERENCE, CODE, DESCRIPTION
from gcal_api import EventGcalAPI

from utils import EventCreationStates


@dp.message_handler(state=EventCreationStates.confirmation)
async def result_confirmation(message: types.Message, state: FSMContext):
    text = message.text
    if text.encode() == b"\xf0\x9f\x91\x8d Yes" or text.strip().lower() in (
        "yes",
        "да",
    ):

        await (
            await message.answer(".", reply_markup=ReplyKeyboardRemove())
        ).delete()
        state_event = await state.get_data()
        # Adding event into db
        last_first_name = (
            f"{message.from_user.last_name} {message.from_user.first_name}"
        )

        date_time = datetime.fromisoformat(state_event[DATE])
        date_time = date_time.replace(
            hour=int(state_event[TIME][HOUR]),
            minute=int(state_event[TIME][MINUTE]),
        )

        user = await UserAccess.query_by_telegram_user_id(
            telegram_user_id=message.from_user.id
        )

        db_event = await EventAccess.create(
            summary=last_first_name,
            start=date_time,
            conference_link=state_event[CONFERENCE],
            document_link=state_event[CODE],
            description=state_event[DESCRIPTION],
            user_id=user.id,
        )
        await state.reset_state(with_data=True)

        await message.answer(
            f"{db_event.id}\n"
            f"{db_event.summary}\n"
            f"{db_event.start}\n"
            f"{db_event.conference_link}\n"
            f"{db_event.document_link}\n"
            f"{db_event.description}\n"
            f"{db_event.google_calendar_event_id}"
        )

        # Adding event into google calendar

        conference_link = (
            f'<a href="{db_event.conference_link}">Conference link</a>'
        )

        document_link = f'<a href="{db_event.document_link}">Document link</a>'

        public_description = (
            f"{conference_link}\n{document_link}\n" f"{db_event.description}"
        )

        gcal_event = EventGcalAPI.create(
            event_id=db_event.google_calendar_event_id,
            summary=db_event.summary,
            start=db_event.start,
            description=public_description,
        )

        await message.answer(
            f"{gcal_event.event_id}\n"
            f"{gcal_event.summary}\n"
            f"{gcal_event.start}\n"
            f"{gcal_event.description}\n"
            f"{gcal_event.location}"
        )

    elif text.encode() == b"\xf0\x9f\x91\x8e No" or text.strip().lower() in (
        "no",
        "нет",
    ):

        await (
            await message.answer(".", reply_markup=ReplyKeyboardRemove())
        ).delete()

        await state.reset_state(with_data=True)

    else:
        await message.answer("Используйте предлагаемую клавиатуру")
