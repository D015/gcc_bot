from aiogram import types

from aiogram.dispatcher.filters.state import State, StatesGroup

from gcc_app.constants import DATE, TIME, CONFERENCE, CODE, DESCRIPTION
from gcc_app.keyboards import create_calendar


class EventCreationStates(StatesGroup):
    date = State()
    time = State()
    conference = State()
    code = State()
    description = State()
    confirmation = State()


async def continue_for_start():
    pass


async def continue_for_date(message: types.Message):
    return await message.answer(f"Выберите, пожалуйста, дату:",
                                reply_markup=create_calendar())


requests_to_user = {
    DATE: continue_for_date,
    TIME: 'EVENT_TIME',
    CONFERENCE: 'CONFERENCE_LINK',
    CODE: 'S_4_EVENT_CODE',
    DESCRIPTION: 'CONFERENCE_LINK',
    'confirmation': 'CONFERENCE_LINK',
}
