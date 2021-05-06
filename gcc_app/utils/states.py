from aiogram.utils.helper import Helper, HelperMode, ListItem


class States(Helper):
    mode = HelperMode.snake_case

    _0_CREATE_EVENT_STATE = ListItem()
    _1_EVENT_DATE_STATE = ListItem()
    _2_EVENT_TIME_STATE = ListItem()
    _3_CONFERENCE_LINK_STATE = ListItem()
    _4_EVENT_CODE_STATE = ListItem()
    _5_EVENT_DESCRIPTION_STATE = ListItem()
    _6_EVENT_CONFIRMED_STATE = ListItem()