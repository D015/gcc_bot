from aiogram import types

from gcc_app.app import dp, bot
from gcc_app.constants import (KEY_UNFINISHED_EVENT_CREATION,
                               CONFERENCE_LINK, YES_CONFIRMATION, NO_REFUSAL)
from gcc_app.global_utils import (redis_get,
                                  redis_set, test_print)
from gcc_app.keyboards import create_confirmation_board
from gcc_app.utils import States
from gcc_app.utils.find_bad_words import find_bad_words


@dp.callback_query_handler(lambda c: c.data, state=States.S_4_EVENT_CODE)
async def process_confirmed_intent_description(
        callback_query: types.CallbackQuery):

    data = callback_query.data
    state = dp.current_state(user=callback_query.from_user.id)
    if data == YES_CONFIRMATION:
        await state.set_state(States.all()[5])
        await bot.answer_callback_query(callback_query.id,
                                        text='Введите описание встречи')
        await callback_query.message.delete_reply_markup()
    elif data == NO_REFUSAL:
        await state.set_state(States.all()[6])
        await bot.answer_callback_query(callback_query.id)
        await callback_query.message.delete_reply_markup()
        await bot.send_message(callback_query.from_user.id,
                               # todo add all entered event parameters
                               text='Опубликовать встречу?',
                               reply_markup=create_confirmation_board())
    else:
        await state.set_state(States.all()[6])
        await bot.answer_callback_query(callback_query.id,
                                        text='Использован нестандартный ответ.')
        await callback_query.message.delete_reply_markup()
        await bot.send_message(callback_query.from_user.id,
                               # todo add all entered event parameters
                               text='Опубликовать встречу?',
                               reply_markup=create_confirmation_board())


@dp.message_handler(state=States.S_4_EVENT_CODE)
async def process_event_description(message: types.Message):
    text = message.text
    if not (await find_bad_words(text)):
        await message.reply("Ваша описание принята")
        redis_name = \
            f'{message.from_user.id}_{KEY_UNFINISHED_EVENT_CREATION}'

        unfinished_event_creation: dict = redis_get(redis_name)
        unfinished_event_creation.update({CONFERENCE_LINK: text})
        redis_set(redis_name, unfinished_event_creation)
        state = dp.current_state(user=message.from_user.id)
        await state.set_state(States.all()[5])
        await message.answer('Введите ссылку на обсуждаемый code')
    else:
        await message.answer('Повторите, пожалуйста, описание встречи'
                             ' используя только цензурные слова и фраз.')
