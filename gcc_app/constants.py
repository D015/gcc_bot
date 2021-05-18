import os
from typing import Union

from gcc_app.global_utils import ReaderTXT

DEFAULT_SUMMARY: str = 'Untitled'

# Default delta in hours between start and time.now()
DEFAULT_DELTA_START_AND_NOW: Union[float, int] = 1
NUMBER_OF_HOURS_IN_BOARD = 6
PART_DAY_INDICES = set(range(4))
TIME_BOARD_PART_INDEX = 3
KEY_UNFINISHED_EVENT_CREATION = 'unfinished_event_creation'

NAVIGATION = 'navigation'
TIME_TEXT = 'time_text'

CONFERENCE_LINK = 'conference_link'
CODE_LINK = 'code_link'

YES_CONFIRMATION = 'YES_CONFIRMATION'
NO_REFUSAL = 'NO_REFUSAL'

EVENT_DESCRIPTION_LENGTH = 180
EVENT_TITLE_LENGTH = 60

APP_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
BAD_WORDS_FILE_ROOT = 'data/bad_words.txt'
BAD_WORDS_FILE = os.path.join(APP_ROOT, BAD_WORDS_FILE_ROOT)
BAD_WORDS = ReaderTXT(BAD_WORDS_FILE).read_txt_into_frozenset()