import datetime
from typing import Optional, Union

from aiogram import types
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup

from gcc_app.constants import DATE, TIME, CONFERENCE, CODE, DESCRIPTION, \
    TEXT, REPLY_MARKUP, CONFIRMATION
from gcc_app.global_utils import DateTameStr
from gcc_app.keyboards import create_calendar, create_time_board, \
    create_confirmation_board


class EventCreationStates(StatesGroup):
    date = State()
    time = State()
    conference = State()
    code = State()
    description = State()
    confirmation = State()


async def go_to_next(state: FSMContext) -> str:
    state_class_name = (await state.get_state()).split(':')[0]
    state_class = globals().get(state_class_name)
    next_state = await state_class.next()
    next_state_name = next_state.split(':')[1]
    return next_state_name


async def save_state_data(
        state: FSMContext, data: Union[str, int, dict, datetime.datetime]):
    data_key = (await state.get_state()).split(':')[1]
    data = DateTameStr(data) if type(data) == datetime.datetime else data
    print(type(data))
    await state.update_data({data_key: data})


async def continue_for_next(
        message: types.Message,
        text: str = '',
        reply_markup: Optional[InlineKeyboardMarkup] = None):
    await message.answer(text=text, reply_markup=reply_markup)


async def save_and_continue(
        message: types.Message,
        state: FSMContext,
        data: Union[str, int, dict]):
    await save_state_data(state=state, data=data)

    next_state_name = await go_to_next(state=state)
    next_text = requests_to_user[next_state_name].get(TEXT)
    next_reply_markup = requests_to_user[next_state_name].get(REPLY_MARKUP)

    await continue_for_next(
        message=message, text=next_text, reply_markup=next_reply_markup)


requests_to_user = {
    DATE: {TEXT: "Выберите дату:", REPLY_MARKUP: create_calendar()},
    TIME: {TEXT: "Выберите время:", REPLY_MARKUP: create_time_board()},
    CONFERENCE: {TEXT: "Введите ссылку на онлайн-конференции"},
    CODE: {TEXT: "Введите ссылку на обсуждаемый code"},
    DESCRIPTION: {TEXT: "Введите описание встречи."},
    CONFIRMATION: {TEXT: "Опубликовать встречу?",
                   REPLY_MARKUP: create_confirmation_board()},
}
