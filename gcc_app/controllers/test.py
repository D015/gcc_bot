from aiogram import types

from access import EventAccess
from access import UserAccess
from app import dp
from gcal_api import EventGcalAPI
from models import UserModel
from models import EventModel


@dp.message_handler(commands=["test"])
async def process_test_command(message: types.Message):
    user_id = (
        UserAccess(telegram_user_id=message.from_user.id)
        .query_by_telegram_user_id()
        .id
    )
    # user_new = UserModel(telegram_user_id=456)
    # session.add(user_new)
    # session.flush()
    # events_new = EventModel()
    # session.add(events_new)
    # r = session.commit()
    # print(events_new)
    # # print(type(message.from_user.id))
    # # print(type(message.from_user.is_bot))
    # # user_new_id = UserAccess(telegram_user_id=32111).create()
    # # print(user_new_id)
    # event_model_new = EventAccess(user_id=1).create()

    # print(event_model_new.google_calendar_event_id)
    # print(type(event_model_new.google_calendar_event_id))
    # event_new = \
    # EventGcalAPI(event_id=event_model_new.google_calendar_event_id).create()

    # user = UserAccess(telegram_user_id=32111).query_by_telegram_user_id()
    # event = EventAccess(
    #     google_calendar_event_id='32111').query_by_google_calendar_event_id()
    # print(user)
    # print(event)
    # print('--------------------------')
    # user = UserAccess(id=24).query_by_id()
    # event = EventAccess(id=25).query_by_id()
    # print(user)
    # print(event)
    # print('--------------------------')
    # deactivate_res = EventAccess(_obj=event).deactivate()
    # archive_res = EventAccess(_obj=event).archive()
    # print(deactivate_res)
    # print(archive_res)
    # print('--------------------------')
    # user_remove_res = UserAccess(_obj=user).remove()
    # event_remove_res = EventAccess(_obj=event).remove()
    # print(user_remove_res)
    # print(event_remove_res)

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

    # await message.reply(f"Привет!\n Это тест!\ndb - {event_model_new}\ngc - {event_new}")
    await message.reply(f"Привет!\n Это тест! {user_id}")
