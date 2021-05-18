from aiogram import types
from aiogram.types import callback_query

from gcc_app.app import dp
from gcc_app.constants import (KEY_UNFINISHED_EVENT_CREATION, CODE_LINK)
from gcc_app.global_utils import (redis_get,
                                  redis_set)
from gcc_app.keyboards import create_confirmation_board
from gcc_app.utils import States


@dp.message_handler(state=States.S_3_CONFERENCE_LINK)
async def process_code_link(message: types.Message):
    text = message.text
    if text.startswith('http') and '.' in text and '//' in text:

        await message.reply("Ваша ссылка на code принята")
        redis_name = \
            f'{message.from_user.id}_{KEY_UNFINISHED_EVENT_CREATION}'

        unfinished_event_creation: dict = redis_get(redis_name)
        unfinished_event_creation.update({CODE_LINK: text})
        redis_set(redis_name, unfinished_event_creation)
        state = dp.current_state(user=message.from_user.id)
        await state.set_state(States.all()[4])
        await message.answer('Хотите добавить описание встречи?',
                             reply_markup=create_confirmation_board())

    else:
        await message.answer('Введите ссылку на обсуждаемый code\n'
                             'это должно быть URI '
                             'и начинаться с "http" или "https"')
