from aiogram import types

from app import dp
from constants import TEXT, REPLY_MARKUP
from utils import EventCreationStates, continue_for_next
from utils import requests_to_user


@dp.message_handler(state="*", commands=["create_event"])
async def process_create_event_command(message: types.Message):
    first_state1 = await EventCreationStates.first()
    next_state_name = first_state1.split(":")[1]
    next_text = requests_to_user[next_state_name].get(TEXT)
    next_reply_markup = requests_to_user[next_state_name].get(REPLY_MARKUP)

    await continue_for_next(
        message=message, text=next_text, reply_markup=next_reply_markup
    )
