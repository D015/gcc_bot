from aiogram import types

from aiogram.dispatcher.filters.state import State, StatesGroup

from gcc_app.constants import DATE, TIME, CONFERENCE, CODE, DESCRIPTION
from gcc_app.keyboards import create_calendar, create_time_board


class EventCreationStates(StatesGroup):
    date = State()
    time = State()
    conference = State()
    code = State()
    description = State()
    confirmation = State()


async def continue_for_date(message: types.Message):
    return await message.answer("Выберите дату:",
                                reply_markup=create_calendar())


async def continue_for_time(message: types.Message):
    return await message.answer("Выберите время:",
                                reply_markup=create_time_board())


async def continue_for_conference(message: types.Message):
    return await message.answer("Введите ссылку на онлайн-конференции")


requests_to_user = {
    DATE: continue_for_date,
    TIME: continue_for_time,
    CONFERENCE: continue_for_conference,
    CODE: 'S_4_EVENT_CODE',
    DESCRIPTION: 'CONFERENCE_LINK',
    'confirmation': 'CONFERENCE_LINK',
}
