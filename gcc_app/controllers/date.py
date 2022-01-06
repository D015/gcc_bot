from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from app import dp, bot
from utils import EventCreationStates
from keyboards import calendar_callback, process_calendar_selection
from utils import save_and_continue


@dp.callback_query_handler(calendar_callback.filter(), state=EventCreationStates.date)
async def result_calendar(
    callback_query: CallbackQuery, callback_data: dict, state: FSMContext
):
    selected, event_date = await process_calendar_selection(
        callback_query, callback_data
    )
    print(type(EventCreationStates))

    if selected:
        date: str = event_date.strftime("%d/%m/%Y")
        await bot.answer_callback_query(callback_query.id, text=date)
        await callback_query.message.answer(f"Выбрано {date}")
        await save_and_continue(
            message=callback_query.message,
            state=state,
            state_class=EventCreationStates,
            data=event_date,
        )
