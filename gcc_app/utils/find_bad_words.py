from typing import Optional

from gcc_app.constants import BAD_WORDS


async def find_bad_words(text: str, bad_words: frozenset = BAD_WORDS) -> Optional[str]:
    for word in bad_words:
        if word in text.split(" "):
            return word
    return None
