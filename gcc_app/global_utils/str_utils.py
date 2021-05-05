from typing import Optional


def convert_str_to_int(data: str) -> Optional[int]:
    return int(data) if data.isdigit() else None

print(convert_str_to_int('0'))