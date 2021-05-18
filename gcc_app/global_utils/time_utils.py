import re
from typing import Union

from gcc_app.constants import HOUR, MINUTE


def get_time_from_string(text: str) -> Union[dict, float]:
    digits: list = re.findall(r'(\d+)', text)
    if len(digits) == 2:
        hour: int = int(digits[0])
        minute: int = int(digits[1])
        if 0 <= hour <= 24 and 0 <= minute <= 60:
            time_from_string = {HOUR: hour, MINUTE: minute}
            return time_from_string
    return False
