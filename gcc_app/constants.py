from datetime import datetime
from typing import Union

from gcc_app.utils import create_default_start

default_summary: str = 'Untitled'

# Default delta in hours between start and time.now()
default_delta_start_and_now: Union[float, int] = 1
default_start: datetime = create_default_start()
