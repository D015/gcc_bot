from aiogram import types

from gcc_app.access.event import EventAccess
from gcc_app.access.user import UserAccess
from gcc_app.app import session, dp
from gcc_app.models import UserModel
from gcc_app.models.event import EventModel
from gcc_app.utils import States
from gcc_app.views.aiogramcalendar import create_calendar


@dp.message_handler(state='*', commands=['create_event'])
async def process_create_event_command(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(States.all()[int('0')])

    await message.answer("Выберите, пожалуйста, дату: ",
                         reply_markup=create_calendar())
