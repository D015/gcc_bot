from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from gcc_app.access.event import EventAccess
from gcc_app.access.user import UserAccess
from gcc_app.app import dp
from gcc_app.constants import DATE, TIME, HOUR, MINUTE, CONFERENCE, CODE, \
    DESCRIPTION

from gcc_app.utils import EventCreationStates


@dp.message_handler(state=EventCreationStates.confirmation)
async def result_confirmation(message: types.Message, state: FSMContext):
    text = message.text
    if text.encode() == b'\xf0\x9f\x91\x8d Yes' \
            or text.strip().lower() in ('yes', 'да'):

        await (await message.answer('.', reply_markup=ReplyKeyboardRemove())). \
            delete()
        state_event = await state.get_data()

        last_first_name = \
            f'{message.from_user.last_name} {message.from_user.last_name}'

        date_time = datetime.fromisoformat(state_event[DATE])
        date_time.replace(hour=int(state_event[TIME][HOUR]),
                          minute=int(state_event[TIME][MINUTE]))

        user_id = UserAccess(telegram_user_id=message.from_user.id).\
            query_by_telegram_user_id().id

        new_event = EventAccess(summary=last_first_name,
                                start=date_time,
                                conference_link=state_event[CONFERENCE],
                                document_link=state_event[CODE],
                                description=state_event[DESCRIPTION],
                                user_id=user_id).create()
        await state.reset_state(with_data=True)

        print(f'state {await state.get_state()}')
        print(f'data {await state.get_data()}')

        await message.answer(f"{new_event.id}\n"
                             f"{new_event.summary}\n"
                             f"{new_event.start}\n"
                             f"{new_event.conference_link}\n"
                             f"{new_event.document_link}\n"
                             f"{new_event.description}\n"
                             f"{new_event.google_calendar_event_id}")

        # conference_link = \
        #     f'<a href="{state_event[CONFERENCE]}">Conference link</a>'
        #
        # document_link = \
        #     f'<a href="{state_event[CODE]}">Conference link</a>'
        #
        # public_description =

    elif text.encode() == b'\xf0\x9f\x91\x8e No' \
            or text.strip().lower() in ('no', 'нет'):

        await (await message.answer('.', reply_markup=ReplyKeyboardRemove())). \
            delete()
