from aiogram import types

from gcc_app.access.event import EventAccess
from gcc_app.access.user import UserAccess
from gcc_app.app import session, dp
from gcc_app.models import UserModel
from gcc_app.models.event import EventModel


@dp.message_handler(commands=['create_event'])
async def process_test_command(message: types.Message):

    # user_new = User(telegram_user_id=456)
    # session.add(user_new)
    # session.flush()
    # events_new = Event(google_calendar_event_id='456', user_id=user_new.id)
    # session.add(events_new)
    # session.commit()
    # print(type(message.from_user.id))
    # print(type(message.from_user.is_bot))
    # user_new_id = UserAccess(telegram_user_id=32111).create()
    # print(user_new_id)
    # EventAccess(google_calendar_event_id='32111', user_id=user_new_id).create()
    user = UserAccess(telegram_user_id=32111).query_by_telegram_user_id()
    event = EventAccess(
        google_calendar_event_id='32111').query_by_google_calendar_event_id()
    print(user)
    print(event)
    print('--------------------------')
    user = UserAccess(id=24).query_by_id()
    event = EventAccess(id=25).query_by_id()
    print(user)
    print(event)
    print('--------------------------')
    deactivate_res = EventAccess(_obj=event).deactivate()
    archive_res = EventAccess(_obj=event).archive()
    print(deactivate_res)
    print(archive_res)
    print('--------------------------')
    user_remove_res = UserAccess(_obj=user).remove()
    event_remove_res = EventAccess(_obj=event).remove()
    print(user_remove_res)
    print(event_remove_res)




    # user = session.query(User).filter_by(chat_id=321).first()
    # print('--------------------')
    # print(user)
    # print('--------------------')
    # print(user.events.all())
    # print('--------------------')
    # print('--------------------')
    #
    # event = session.query(Event).filter_by(event_id='123').first()
    # print('--------------------')
    # print(event)
    # print('--------------------')
    # print(event.user)

    await message.reply(f"Привет!\nНапиши мне что-нибудь!\n"
                        f"{deactivate_res}\n"
                        f"{archive_res}")