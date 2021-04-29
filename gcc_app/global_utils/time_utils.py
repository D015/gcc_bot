import re
from typing import Any, Union


def get_time_from_string(text: str) -> Union[dict, float]:
    digits: list = re.findall(r'(\d+)', text)
    if len(digits) == 2:
        hour: int = int(digits[0])
        minute: int = int(digits[1])
        if 0 <= hour <= 24 and 0 <= minute <= 60:
            time_from_string = {'hour': hour, 'minute': minute}
            return time_from_string
    return False


