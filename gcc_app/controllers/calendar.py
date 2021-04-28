import pickle

from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from gcc_app.app import dp, redis_db
from gcc_app.global_utils import test_print, redis_set, redis_get

from gcc_app.utils import States
from gcc_app.views.aiogramcalendar import (calendar_callback,
                                           process_calendar_selection)


@dp.callback_query_handler(calendar_callback.filter(),
                           state=States.CREATE_EVENT_STATE_0)
async def result_calendar(callback_query: CallbackQuery, callback_data: dict):
    selected, date_time = await process_calendar_selection(callback_query,
                                                      callback_data)
    test_print(date_time)

    redis_name = f'{callback_query.from_user.id}_unfinished_event_creation'
    unfinished_event_creation: dict = redis_get(redis_name)
    test_print(unfinished_event_creation)
    unfinished_event_creation.update({'date_time': date_time})
    redis_set(redis_name, unfinished_event_creation)

    if selected:
        state = dp.current_state(user=callback_query.from_user.id)
        await state.set_state(States.all()[int('1')])
        await callback_query.message.answer(
            f"Вы выбрали {date_time.strftime('%d/%m/%Y')}\n"
            f"Напишите, пожалуйста, время используя цифры "
            f"(можно использовать какой-нибудь не цифровой разделитель"
            f"между часами и минутами)",
            reply_markup=ReplyKeyboardRemove())
