from typing import Union

from aiogram import types

from gcc_app.app import dp, bot
from gcc_app.constants import key_unfinished_event_creation, navigation, \
    part_day_indices, time_text
from gcc_app.global_utils import test_print, redis_get, get_time_from_string, \
    redis_set, convert_str_to_int
from gcc_app.keyboards import create_time_board
from gcc_app.utils import States


@dp.callback_query_handler(lambda c: c.data, state=States.EVENT_DATE_STATE_1)
async def callback_time(callback_query: types.CallbackQuery):
    event_time: Union[dict, float] = get_time_from_string(callback_query.data)
    if event_time:
        await bot.answer_callback_query(callback_query.id,
                                        text=callback_query.data)
        await callback_query.message.delete_reply_markup()

        redis_name = \
            f'{callback_query.from_user.id}_{key_unfinished_event_creation}'
        unfinished_event_creation: dict = redis_get(redis_name)

        event_date_time = unfinished_event_creation['date_time'].replace(
            hour=event_time['hour'], minute=event_time['minute'])
        unfinished_event_creation['date_time'] = event_date_time
        redis_set(redis_name, unfinished_event_creation)

        state = dp.current_state(user=callback_query.from_user.id)
        await state.set_state(States.all()[int('2')])

        await callback_query.message.answer(f"Вы выбрали {callback_query.data}")
    elif callback_query.data.startswith(navigation):
        other_part_index = callback_query.data.split('_')[1]
        other_part_index = convert_str_to_int(other_part_index)
        if other_part_index is not None \
                and other_part_index in part_day_indices:
            await callback_query.message.edit_reply_markup(
                reply_markup=create_time_board(other_part_index))
    elif callback_query.data == time_text:
        await callback_query.message.delete_reply_markup()
        await callback_query.message.answer(
            f"Напишите, пожалуйста, время используя цифры "
            f"и любой нецифровой символ как разделитель "
            f"между часами и минутами")



@dp.message_handler(state=States.EVENT_DATE_STATE_1)
async def result_time(message: types.Message):
    event_time: Union[dict, float] = get_time_from_string(message.text)
    if event_time:
        hour = event_time['hour']
        minute = event_time['minute']
        # todo use it in def callback_time
        hour_text = str(hour) if hour >= 10 else f'0{hour}'
        minute_text = str(minute) if minute >= 10 else f'0{minute}'
        await message.answer(f"Вы ввели: {hour_text}:{minute_text}")
        redis_name = \
            f'{message.from_user.id}_{key_unfinished_event_creation}'
        unfinished_event_creation: dict = redis_get(redis_name)

        event_date_time = unfinished_event_creation['date_time'].replace(
            hour=hour, minute=minute)

        unfinished_event_creation['date_time'] = event_date_time
        redis_set(redis_name, unfinished_event_creation)
        state = dp.current_state(user=message.from_user.id)
        await state.set_state(States.all()[int('2')])
    else:
        await message.answer(f"Некоректный ввод!\n"
                             f"Введите время в формате:\n"
                             f"цифры пробел цифры")
