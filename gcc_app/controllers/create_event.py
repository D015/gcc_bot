from aiogram import types

from gcc_app.app import dp
from gcc_app.constants import TEXT, REPLY_MARKUP
from gcc_app.utils import EventCreationStates, continue_for_next
from gcc_app.utils.creation_dialogue import requests_to_user


@dp.message_handler(state='*', commands=['create_event'])
async def process_create_event_command(message: types.Message):
    first_state = await EventCreationStates.first()
    next_state_name = first_state.split(':')[1]
    next_text = requests_to_user[next_state_name].get(TEXT)
    next_reply_markup = requests_to_user[next_state_name].get(REPLY_MARKUP)

    await continue_for_next(
        message=message, text=next_text, reply_markup=next_reply_markup)
