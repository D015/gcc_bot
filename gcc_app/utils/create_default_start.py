from datetime import datetime, timedelta
from typing import Union

from gcc_app.constants import DEFAULT_DELTA_START_AND_NOW


def create_default_start(
    hours_delta: Union[
            float, int] = DEFAULT_DELTA_START_AND_NOW) -> datetime:
    """Create a time (start of event) different from time.now()
    by delta (hours_delta) in hours"""
    if type(hours_delta) is not float \
            and type(hours_delta) is not int:
        hours_delta = 0
    return datetime.utcnow() + timedelta(hours=hours_delta)
