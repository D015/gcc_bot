from aiogram import types

from gcc_app.app import dp
from gcc_app.constants import (key_unfinished_event_creation,
                               conference_link)
from gcc_app.global_utils import (redis_get,
                                  redis_set, test_print)
from gcc_app.utils import States


@dp.message_handler(state=States._2_EVENT_TIME_STATE)
async def process_conference_link(message: types.Message):
    text = message.text
    if text.startswith('http') and '.' in text and '//' in text:

        await message.reply("Ваша ссылка на онлайн-конференцию принята")
        redis_name = \
            f'{message.from_user.id}_{key_unfinished_event_creation}'

        unfinished_event_creation: dict = redis_get(redis_name)
        unfinished_event_creation.update({conference_link: text})
        redis_set(redis_name, unfinished_event_creation)
        state = dp.current_state(user=message.from_user.id)
        await state.set_state(States.all()[3])
        await message.answer('Введите ссылку на обсуждаемый code')
    else:
        await message.answer('Введите ссылку на онлайн-конференцию\n'
                             'это должно быть URI '
                             'и начинаться с "http" или "https"')
