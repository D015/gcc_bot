from aiogram import types
from aiogram.dispatcher import FSMContext

from gcc_app.app import dp, bot
from gcc_app.constants import YES_CONFIRMATION, NO_REFUSAL
from gcc_app.keyboards import create_confirmation_board
from gcc_app.utils import EventCreationStates
from gcc_app.utils.creation_dialogue import save_and_continue
from gcc_app.utils.find_bad_words import find_bad_words


@dp.message_handler(state=EventCreationStates.description)
async def process_event_description(message: types.Message, state: FSMContext):
    if message.text and not (await find_bad_words(message.text)):
        await save_and_continue(message=message,
                                state=state,
                                state_class=EventCreationStates,
                                data=message.text)
    else:
        await message.answer('Повторите, пожалуйста, описание встречи'
                             ' используя только цензурные слова и фраз.')


@dp.callback_query_handler(lambda c: c.data,
                           state=EventCreationStates.description)
async def process_confirmed_intent_description(
        callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.delete_reply_markup()
    data = callback_query.data
    state = dp.current_state(user=callback_query.from_user.id)

    if data == YES_CONFIRMATION:
        await state.set_state(EventCreationStates.all()[5])
        await bot.send_message(callback_query.from_user.id,
                               text='Введите описание встречи.')
    elif data == NO_REFUSAL:
        await state.set_state(EventCreationStates.all()[6])
        await bot.send_message(callback_query.from_user.id,
                               # todo add all entered event parameters
                               text='Опубликовать встречу?',
                               reply_markup=create_confirmation_board())
    else:
        await state.set_state(EventCreationStates.all()[6])
        await bot.send_message(callback_query.from_user.id,
                               text='Использован нестандартный ответ.\n'
                                    'Он трактуется как "Отказ"')
        await bot.send_message(callback_query.from_user.id,
                               # todo add all entered event parameters
                               text='Опубликовать встречу?',
                               reply_markup=create_confirmation_board())
