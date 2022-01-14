from aiogram import types
from aiogram.dispatcher import FSMContext

from app import dp
from utils import EventCreationStates
from utils import save_and_continue


@dp.message_handler(state=EventCreationStates.code)
async def process_code_link(message: types.Message, state: FSMContext):
    text = message.text
    if text.startswith("http") and "." in text and "//" in text:
        await message.reply("Ваша ссылка на code принята")
        await save_and_continue(
            message=message,
            state=state,
            state_class=EventCreationStates,
            data=text,
        )
    else:
        await message.answer(
            "Введите ссылку на обсуждаемый code\n"
            "это должно быть URI "
            'и начинаться с "http" или "https"'
        )
