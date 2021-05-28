from aiogram.types import (InlineKeyboardMarkup,
                           InlineKeyboardButton, ReplyKeyboardMarkup,
                           KeyboardButton)

from gcc_app.constants import (
                               YES_CONFIRMATION, NO_REFUSAL)


def create_confirmation_board() -> InlineKeyboardMarkup:
    confirmation = InlineKeyboardButton("YES", callback_data=YES_CONFIRMATION)
    refusal = InlineKeyboardButton("NO", callback_data=NO_REFUSAL)
    confirmation_kb = InlineKeyboardMarkup(
        row_width=2).add(confirmation, refusal)
    return confirmation_kb


def create_confirmation_button() -> ReplyKeyboardMarkup:
    button_yes = KeyboardButton('👍 Yes')
    button_no = KeyboardButton('👎 No')
    print('👍 Yes'.encode())
    print('👎 No'.encode())

    confirmation_kb = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True).\
        add(button_yes, button_no)
    return confirmation_kb



