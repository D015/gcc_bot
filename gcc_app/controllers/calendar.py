import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils import executor

from gcc_app.app import dp
from gcc_app.utils import States
from gcc_app.views.aiogramcalendar import (calendar_callback,
                                           create_calendar,
                                           process_calendar_selection)


@dp.message_handler(state=States.CREATE_EVENT_STATE_0)
async def process_calendar(message: Message):
    await message.answer("Please select a date: ", reply_markup=create_calendar())


@dp.callback_query_handler(calendar_callback.filter(), state=States.CREATE_EVENT_STATE_0)
async def result_calendar(callback_query: CallbackQuery, callback_data: dict):
    print(callback_query)
    print(callback_data)

    selected, date = await process_calendar_selection(callback_query, callback_data)
    if selected:
        state = dp.current_state(user=callback_query.from_user.id)
        await state.set_state(States.all()[int('1')])
        await callback_query.message.answer(f'You selected {date.strftime("%d/%m/%Y")}', reply_markup=ReplyKeyboardRemove())
