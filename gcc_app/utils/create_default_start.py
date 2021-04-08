from datetime import datetime, timedelta
from typing import Union

# from gcc_app.constants import default_delta_start_and_now


def create_default_start(
        hours_delta: Union[
            float, int] = 1) -> datetime:
    """Create a time (start of event) different from time.now()
    by delta (hours_delta) in hours"""
    if type(hours_delta) is not float \
            and type(hours_delta) is not int:
        hours_delta = 0
    return datetime.now() + timedelta(hours=hours_delta)
