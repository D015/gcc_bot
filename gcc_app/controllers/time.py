from typing import Union

from aiogram import types

from gcc_app.app import dp
from gcc_app.global_utils import test_print, redis_get, get_time_from_string, \
    redis_set
from gcc_app.utils import States


@dp.message_handler(state=States.EVENT_DATE_STATE_1)
async def result_time(message: types.Message):
    event_time: Union[dict, float] = get_time_from_string(message.text)
    if event_time:
        redis_name = f'{message.from_user.id}_unfinished_event_creation'
        unfinished_event_creation: dict = redis_get(redis_name)

        event_date_time = unfinished_event_creation['date_time'].replace(
            hour=event_time['hour'], minute=event_time['minute'])

        unfinished_event_creation['date_time'] = event_date_time
        redis_set(redis_name, unfinished_event_creation)
        state = dp.current_state(user=message.from_user.id)
        await state.set_state(States.all()[int('2')])
        test_print(redis_get(redis_name))
    else:
        pass

