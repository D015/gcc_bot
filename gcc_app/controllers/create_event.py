from aiogram import types
from aiogram.dispatcher import FSMContext, filters

from gcc_app.app import dp
from gcc_app.constants import KEY_UNFINISHED_EVENT_CREATION
from gcc_app.global_utils import redis_set
from gcc_app.utils import EventCreationStates
from gcc_app.keyboards import create_calendar
from gcc_app.utils.creation_dialogue import requests_to_user


@dp.message_handler(state='*', commands=['create_event'])
async def process_create_event_command(message: types.Message):
    redis_name = f'{message.from_user.id}_{KEY_UNFINISHED_EVENT_CREATION}'
    redis_set(redis_name, {})
    first_state = await EventCreationStates.first()
    function_key = first_state.split(':')[1]
    await requests_to_user[function_key](message)
