from aiogram.utils.helper import Helper, HelperMode, ListItem


class States(Helper):
    mode = HelperMode.snake_case

    S_0_CREATE_EVENT = ListItem()
    S_1_EVENT_DATE = ListItem()
    S_2_EVENT_TIME = ListItem()
    S_3_CONFERENCE_LINK = ListItem()
    S_4_EVENT_CODE = ListItem()
    S_5_CONFIRMED_INTENT_DESCRIPTION = ListItem()
    S_6_NOT_CONFIRMED_INTENT_DESCRIPTION = ListItem()
    S_7_EVENT_DESCRIPTION = ListItem()
    S_8_CONFIRMED_EVENT = ListItem()
