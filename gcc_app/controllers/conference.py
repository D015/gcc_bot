from aiogram import types

from gcc_app.app import dp
from gcc_app.constants import (KEY_UNFINISHED_EVENT_CREATION,
                               CONFERENCE_LINK)
from gcc_app.global_utils import (redis_get,
                                  redis_set, test_print)
from gcc_app.utils import States


@dp.message_handler(state=States.S_2_EVENT_TIME)
async def process_conference_link(message: types.Message):
    text = message.text
    if text.startswith('http') and '.' in text and '//' in text:

        await message.reply("Ваша ссылка на онлайн-конференцию принята")
        redis_name = \
            f'{message.from_user.id}_{KEY_UNFINISHED_EVENT_CREATION}'

        unfinished_event_creation: dict = redis_get(redis_name)
        unfinished_event_creation.update({CONFERENCE_LINK: text})
        redis_set(redis_name, unfinished_event_creation)
        state = dp.current_state(user=message.from_user.id)
        await state.set_state(States.all()[3])
        await message.answer('Введите ссылку на обсуждаемый code')
    else:
        await message.answer('Введите ссылку на онлайн-конференцию\n'
                             'это должно быть URI '
                             'и начинаться с "http" или "https"')
