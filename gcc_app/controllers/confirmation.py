from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from gcc_app.access.event import EventAccess
from gcc_app.app import dp
from gcc_app.constants import DATE, TIME, HOUR, MINUTE

from gcc_app.utils import EventCreationStates


@dp.message_handler(state=EventCreationStates.confirmation)
async def result_confirmation(message: types.Message, state: FSMContext):
    text = message.text
    if text.encode() == b'\xf0\x9f\x91\x8d Yes' \
            or text.strip().lower() in ('yes', 'да'):

        await (await message.answer('.', reply_markup=ReplyKeyboardRemove())).\
            delete()

        state_event = await state.get_data()
        event_datetime = datetime.fromisoformat(state_event[DATE])
        event_datetime.replace(hour=state_event[TIME][HOUR],
                               minute=state_event[TIME][MINUTE])


        new_event = EventAccess().create()

        await message.answer(f"{new_event.id}\n"
                             f"{new_event.summary}\n"
                             f"{new_event.start}\n"
                             f"{new_event.conference_link}\n"
                             f"{new_event.document_link}\n"
                             f"{new_event.description}\n"
                             f"{new_event.google_calendar_event_id}")
    elif text.encode() == b'\xf0\x9f\x91\x8e No' \
            or text.strip().lower() in ('no', 'нет'):

        await (await message.answer('.', reply_markup=ReplyKeyboardRemove())). \
            delete()
