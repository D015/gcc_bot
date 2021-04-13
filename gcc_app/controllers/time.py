from aiogram import types
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from gcc_app.app import dp
from gcc_app.utils import States
from gcc_app.views.aiogramcalendar import (calendar_callback,
                                           process_calendar_selection)


@dp.message_handler(state=States.EVENT_DATE_STATE_1)
async def result_time(message: types.Message):
    text = message.text
    print(text)
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(States.all()[int('2')])
