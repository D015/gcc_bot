from aiogram import types

from gcc_app.app import dp
from gcc_app.global_utils import redis_set
from gcc_app.utils import States
from gcc_app.keyboards import create_calendar


@dp.message_handler(state='*', commands=['create_event'])
async def process_create_event_command(message: types.Message):
    key = f'{message.from_user.id}_unfinished_event_creation'
    redis_set(key, {})
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(States.all()[int('0')])

    await message.answer(f"Выберите, пожалуйста, дату:",
                         reply_markup=create_calendar())
