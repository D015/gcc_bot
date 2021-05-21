from aiogram.types import CallbackQuery

from gcc_app.app import dp, bot
from gcc_app.constants import KEY_UNFINISHED_EVENT_CREATION, DATE
from gcc_app.global_utils import redis_set, redis_get

from gcc_app.utils import EventCreationStates
from gcc_app.keyboards import (calendar_callback,
                               process_calendar_selection, create_time_board)
from gcc_app.utils.creation_dialogue import requests_to_user


@dp.callback_query_handler(calendar_callback.filter(),
                           state=EventCreationStates.date)
async def result_calendar(callback_query: CallbackQuery, callback_data: dict):
    selected, event_date = await process_calendar_selection(callback_query,
                                                            callback_data)

    redis_name = \
        f'{callback_query.from_user.id}_{KEY_UNFINISHED_EVENT_CREATION}'
    unfinished_event_creation: dict = redis_get(redis_name)
    unfinished_event_creation.update({DATE: event_date})
    redis_set(redis_name, unfinished_event_creation)

    if selected:
        await bot.answer_callback_query(callback_query.id,
                                        text=event_date.strftime('%d/%m/%Y'))
        await callback_query.message.answer(
            f"Вы выбрали {event_date.strftime('%d/%m/%Y')}")

        next_state = await EventCreationStates.next()
        function_key = next_state.split(':')[1]
        await requests_to_user[function_key](callback_query.message)
