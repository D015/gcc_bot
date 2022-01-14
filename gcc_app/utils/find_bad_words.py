import string
from typing import Optional, FrozenSet

from app import BAD_WORDS


async def find_bad_words(
    text: str, bad_words_collection: frozenset = BAD_WORDS
) -> FrozenSet:
    # remove punctuation marks or ( text = re.sub(r'[^\w\s]','',text) )
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = frozenset(text.strip().split(" "))
    bad_words_of_text = text.intersection(bad_words_collection)
    return bad_words_of_text
