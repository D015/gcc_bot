from aiogram.types import (InlineKeyboardMarkup,
                           InlineKeyboardButton)

from gcc_app.constants import (TIME_BOARD_PART_INDEX,
                               NUMBER_OF_HOURS_IN_BOARD,
                               PART_DAY_INDICES, NAVIGATION, TIME_TEXT)


def create_time_board(
        part_number: int = TIME_BOARD_PART_INDEX) -> InlineKeyboardMarkup:
    part_start = NUMBER_OF_HOURS_IN_BOARD * part_number
    part_end = part_start + NUMBER_OF_HOURS_IN_BOARD
    time_kb = InlineKeyboardMarkup(row_width=4)
    buttons = []
    for i_hour in range(part_start, part_end):
        for i_i_minute in ('00', '30'):
            i_button = InlineKeyboardButton(
                f'{i_hour}:{i_i_minute}',
                callback_data=f'{i_hour}:{i_i_minute}')
            buttons.append(i_button)
    time_kb.add(*buttons)
    min_part_i = min(PART_DAY_INDICES)
    max_part_i = max(PART_DAY_INDICES)
    sooner_i = part_number - 1 if part_number != min_part_i else max_part_i
    later_i = part_number + 1 if part_number != max_part_i else min_part_i
    navigation_button_sooner = InlineKeyboardButton(
        "Раньше", callback_data=f'{NAVIGATION}_{sooner_i}')
    navigation_button_later = InlineKeyboardButton(
        "Позже", callback_data=f'{NAVIGATION}_{later_i}')
    navigation_button_text = InlineKeyboardButton(
        "Ввести текст", callback_data=TIME_TEXT)
    time_kb.add(navigation_button_sooner,
                navigation_button_text,
                navigation_button_later)
    return time_kb

