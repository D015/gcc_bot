from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from gcc_app.app import dp
from gcc_app.utils import States
from gcc_app.views.aiogramcalendar import (calendar_callback,
                                           process_calendar_selection)


@dp.callback_query_handler(calendar_callback.filter(),
                           state=States.CREATE_EVENT_STATE_0)
async def result_calendar(callback_query: CallbackQuery, callback_data: dict):
    print(callback_query)
    print(callback_data)

    selected, date = await process_calendar_selection(callback_query,
                                                      callback_data)
    if selected:
        state = dp.current_state(user=callback_query.from_user.id)
        await state.set_state(States.all()[int('1')])
        await callback_query.message.answer(
            f"Вы выбрали {date.strftime('%d/%m/%Y')}\n"
            f"Напишите, пожалуйста, время используя цифры "
            f"(можно использовать какой-нибудь не цифровой разделитель между часами и минутами)",
            reply_markup=ReplyKeyboardRemove())
