import pickle

from aiogram import types

from gcc_app.app import dp, redis_db
from gcc_app.utils import States
from gcc_app.views.aiogramcalendar import create_calendar


@dp.message_handler(state='*', commands=['create_event'])
async def process_create_event_command(message: types.Message):
    redis_db.set(message.from_user.id, pickle.dumps({'test': 'test'}))
    test = pickle.loads(redis_db.get(message.from_user.id))['test']
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(States.all()[int('0')])

    await message.answer(f"Выберите, пожалуйста, дату: {test}",
                         reply_markup=create_calendar())
