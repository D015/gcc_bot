from aiogram.dispatcher.filters.state import State, StatesGroup

class States(StatesGroup):

    S_0_CREATE_EVENT = State()
    S_1_EVENT_DATE = State()
    S_2_EVENT_TIME = State()
    S_3_CONFERENCE_LINK = State()
    S_4_EVENT_CODE = State()
    S_5_CONFIRMED_INTENT_DESCRIPTION = State()
    S_6_NOT_CONFIRMED_INTENT_DESCRIPTION = State()
    S_7_EVENT_DESCRIPTION = State()
    S_8_CONFIRMED_EVENT = State()
