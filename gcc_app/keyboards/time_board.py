from aiogram.types import (InlineKeyboardMarkup,
                           InlineKeyboardButton)

from gcc_app.constants import (time_board_part_index,
                               number_of_hours_in_board,
                               part_day_indices, navigation, time_text)


def create_time_board(
        part_number: int = time_board_part_index) -> InlineKeyboardMarkup:
    part_start = number_of_hours_in_board * part_number
    part_end = part_start + number_of_hours_in_board
    time_kb = InlineKeyboardMarkup(row_width=4)
    buttons = []
    for i_hour in range(part_start, part_end):
        for i_i_minute in ('00', '30'):
            i_button = InlineKeyboardButton(
                f'{i_hour}:{i_i_minute}',
                callback_data=f'{i_hour}:{i_i_minute}')
            buttons.append(i_button)
    time_kb.add(*buttons)
    min_part_i = min(part_day_indices)
    max_part_i = max(part_day_indices)
    sooner_i = part_number - 1 if part_number != min_part_i else max_part_i
    later_i = part_number + 1 if part_number != max_part_i else min_part_i
    navigation_button_sooner = InlineKeyboardButton(
        "Раньше", callback_data=f'{navigation}_{sooner_i}')
    navigation_button_later = InlineKeyboardButton(
        "Позже", callback_data=f'{navigation}_{later_i}')
    navigation_button_text = InlineKeyboardButton(
        "Ввести текст", callback_data=time_text)
    time_kb.add(navigation_button_sooner,
                navigation_button_text,
                navigation_button_later)
    return time_kb

