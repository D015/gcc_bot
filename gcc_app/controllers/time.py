from typing import Union

from aiogram import types

from gcc_app.app import dp, bot
from gcc_app.constants import KEY_UNFINISHED_EVENT_CREATION, NAVIGATION, \
    PART_DAY_INDICES, TIME_TEXT, TIME, HOUR, MINUTE
from gcc_app.global_utils import test_print, redis_get, get_time_from_string, \
    redis_set, convert_str_to_int
from gcc_app.keyboards import create_time_board
from gcc_app.utils import EventCreationStates
from gcc_app.utils.creation_dialogue import requests_to_user


@dp.callback_query_handler(lambda c: c.data, state=EventCreationStates.time)
async def callback_time(callback_query: types.CallbackQuery):
    event_time: Union[dict, float] = get_time_from_string(callback_query.data)
    if event_time:
        await bot.answer_callback_query(callback_query.id,
                                        text=callback_query.data)
        await callback_query.message.delete_reply_markup()
        await callback_query.message.answer(f"Вы выбрали {callback_query.data}")

        redis_name = \
            f'{callback_query.from_user.id}_{KEY_UNFINISHED_EVENT_CREATION}'
        unfinished_event_creation: dict = redis_get(redis_name)
        unfinished_event_creation.update({TIME: event_time})
        redis_set(redis_name, unfinished_event_creation)

        next_state = await EventCreationStates.next()
        function_key = next_state.split(':')[1]
        await requests_to_user[function_key](callback_query.message)

    elif callback_query.data.startswith(NAVIGATION):
        other_part_index = callback_query.data.split('_')[1]
        other_part_index = convert_str_to_int(other_part_index)
        if other_part_index is not None \
                and other_part_index in PART_DAY_INDICES:
            await callback_query.message.edit_reply_markup(
                reply_markup=create_time_board(other_part_index))
    elif callback_query.data == TIME_TEXT:
        await callback_query.message.delete_reply_markup()
        await callback_query.message.answer(
            f"Напишите, пожалуйста, время используя цифры "
            f"и любой нецифровой символ как разделитель "
            f"между часами и минутами")


@dp.message_handler(state=EventCreationStates.time)
async def result_time(message: types.Message):
    event_time: Union[dict, float] = get_time_from_string(message.text)
    print(event_time)
    if event_time:
        await message.answer(
            f"Вы ввели: {event_time[HOUR]}:{event_time[MINUTE]}")

        redis_name = \
            f'{message.from_user.id}_{KEY_UNFINISHED_EVENT_CREATION}'
        unfinished_event_creation: dict = redis_get(redis_name)
        unfinished_event_creation.update({TIME: event_time})
        redis_set(redis_name, unfinished_event_creation)

        next_state = await EventCreationStates.next()
        function_key = next_state.split(':')[1]
        await requests_to_user[function_key](message)

    else:
        await message.answer(f"Некорректный ввод!\n"
                             f"Введите время в формате:\n"
                             f"цифры пробел цифры")
