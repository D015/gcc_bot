from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from gcc_app.constants import time_board_part_number, number_of_hours_in_board


def create_time_board(
        part_number: int = time_board_part_number) -> InlineKeyboardMarkup:
    part_start = number_of_hours_in_board * part_number
    part_end = part_start + number_of_hours_in_board
    time_kb = InlineKeyboardMarkup()
    for i_hour in range(part_start, part_end):
        for i_i_minute in ('00', '30'):
            button = InlineKeyboardButton(
                f'{i_hour}:{i_i_minute}',
                callback_data=f'{i_hour}:{i_i_minute}')
            time_kb.add(button)
    return time_kb
