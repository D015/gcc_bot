import datetime
import re
from typing import Union

# from gcc_app.constants import MINUTE, HOUR


def get_time_from_string(text: str) -> Union[dict, float]:
    digits: list = re.findall(r"(\d+)", text)
    if len(digits) == 2:
        hour: int = int(digits[0])
        minute: int = int(digits[1])
        if 0 <= hour <= 24 and 0 <= minute <= 60:
            hour: str = str(hour) if hour >= 10 else f"0{hour}"
            minute: str = str(minute) if minute >= 10 else f"0{minute}"
            time_from_string = {"hour": hour, "minute": minute}
            return time_from_string
    return False


class DateTimeStr(str):
    def __new__(cls, date_time: datetime.datetime):
        return super().__new__(cls, date_time.isoformat())

    def get_datetime(self):
        return datetime.datetime.fromisoformat(self)
