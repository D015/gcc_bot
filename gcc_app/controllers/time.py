from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext

from gcc_app.app import dp, bot
from gcc_app.constants import NAVIGATION, PART_DAY_INDICES, TIME_TEXT, HOUR, MINUTE
from gcc_app.global_utils import get_time_from_string, convert_str_to_int
from gcc_app.keyboards import create_time_board
from gcc_app.utils import EventCreationStates
from gcc_app.utils.creation_dialogue import save_and_continue


@dp.callback_query_handler(lambda c: c.data, state=EventCreationStates.time)
async def callback_time(callback_query: types.CallbackQuery, state: FSMContext):
    message = callback_query.message
    data = callback_query.data
    event_time: Union[dict, float] = get_time_from_string(data)
    if event_time:
        await bot.answer_callback_query(callback_query.id, text=data)
        await message.delete_reply_markup()
        await message.answer(f"Выбрано {data}")
        await save_and_continue(
            message=message,
            state=state,
            state_class=EventCreationStates,
            data=event_time,
        )
    elif data.startswith(NAVIGATION):
        other_part_index = data.split("_")[1]
        other_part_index = convert_str_to_int(other_part_index)
        if other_part_index is not None and other_part_index in PART_DAY_INDICES:
            await message.edit_reply_markup(
                reply_markup=create_time_board(other_part_index)
            )
    elif data == TIME_TEXT:
        await message.delete_reply_markup()
        await message.answer(
            f"Напишите время используя цифры "
            f"и любой нецифровой символ как разделитель "
            f"между часами и минутами"
        )


@dp.message_handler(state=EventCreationStates.time)
async def result_time(message: types.Message, state: FSMContext):
    event_time: Union[dict, float] = get_time_from_string(message.text)
    if event_time:
        await message.answer(f"Введено: {event_time[HOUR]}:{event_time[MINUTE]}")
        await save_and_continue(message=message, state=state, data=event_time)
    else:
        await message.answer(
            f"Некорректный ввод!\n" f"Введите время в формате:\n" f"цифры пробел цифры"
        )
