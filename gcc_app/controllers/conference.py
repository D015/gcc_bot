from aiogram import types
from aiogram.dispatcher import FSMContext

from gcc_app.app import dp
from gcc_app.utils import EventCreationStates
from gcc_app.utils.creation_dialogue import save_and_continue


@dp.message_handler(state=EventCreationStates.conference)
async def process_conference_link(message: types.Message, state: FSMContext):
    text = message.text
    if text.startswith('http') and '.' in text and '//' in text:
        await message.reply("Ваша ссылка на онлайн-конференцию принята")
        await save_and_continue(message=message,
                                state=state,
                                state_class=EventCreationStates,
                                data=text)
    else:
        await message.answer('Введите ссылку на онлайн-конференцию\n'
                             'это должно быть URI '
                             'и начинаться с "http" или "https"')
