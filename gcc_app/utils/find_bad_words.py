from typing import Optional

from gcc_app.constants import BAD_WORDS_FILE
from gcc_app.global_utils import read_txt


def find_bad_words(
        text: str,
        bad_phrases_filed: str = BAD_WORDS_FILE) -> Optional[str]:

    for file_line in read_txt(bad_phrases_filed):
        file_line_list = file_line.split(', ')
        for word in file_line_list:
            if word in text.split(' '):
                return word
    return None


