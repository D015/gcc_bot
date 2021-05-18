from aiogram.types import (InlineKeyboardMarkup,
                           InlineKeyboardButton)

from gcc_app.constants import (
                               YES_CONFIRMATION, NO_REFUSAL)


def create_confirmation_board() -> InlineKeyboardMarkup:
    confirmation_kb = InlineKeyboardMarkup(row_width=2)
    confirmation = InlineKeyboardButton("YES", callback_data=YES_CONFIRMATION)
    refusal = InlineKeyboardButton("NO", callback_data=NO_REFUSAL)
    confirmation_kb.add(confirmation, refusal)
    return confirmation_kb

