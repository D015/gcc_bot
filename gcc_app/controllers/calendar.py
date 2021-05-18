from aiogram.types import CallbackQuery

from gcc_app.app import dp, bot
from gcc_app.constants import KEY_UNFINISHED_EVENT_CREATION
from gcc_app.global_utils import redis_set, redis_get

from gcc_app.utils import States
from gcc_app.keyboards import (calendar_callback,
                               process_calendar_selection, create_time_board)


@dp.callback_query_handler(calendar_callback.filter(),
                           state=States.S_0_CREATE_EVENT)
async def result_calendar(callback_query: CallbackQuery, callback_data: dict):
    selected, event_date = await process_calendar_selection(callback_query,
                                                            callback_data)

    redis_name = \
        f'{callback_query.from_user.id}_{KEY_UNFINISHED_EVENT_CREATION}'
    unfinished_event_creation: dict = redis_get(redis_name)
    unfinished_event_creation.update({'date_time': event_date})
    redis_set(redis_name, unfinished_event_creation)

    if selected:
        state = dp.current_state(user=callback_query.from_user.id)
        await bot.answer_callback_query(callback_query.id,
                                        text=event_date.strftime('%d/%m/%Y'))
        await state.set_state(States.all()[1])
        await callback_query.message.answer(
            f"Вы выбрали {event_date.strftime('%d/%m/%Y')}")
        await callback_query.message.answer(
            f'Выберите, пожалуйста, время:', reply_markup=create_time_board())