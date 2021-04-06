from aiogram import types

from gcc_app.access.user import UserAccess
from gcc_app.app import session, dp
from gcc_app.models import User
from gcc_app.models.event import Event


@dp.message_handler(commands=['test'])
async def process_test_command(message: types.Message):
    # user_new = User(chat_id=456)
    # session.add(user_new)
    # session.commit()
    # events_new = Event(event_id='123', user_id=user_new.id)
    # session.add(events_new)
    # session.commit()
    # print(type(message.from_user.id))
    # print(type(message.from_user.is_bot))
    user = session.query(User).filter_by(chat_id=321).first()
    print('--------------------')
    print(user)
    print('--------------------')
    print(user.events.all())
    print('--------------------')
    print('--------------------')

    event = session.query(Event).filter_by(event_id='123').first()
    print('--------------------')
    print(event)
    print('--------------------')
    print(event.user)

    await message.reply("Привет!\nНапиши мне что-нибудь!")