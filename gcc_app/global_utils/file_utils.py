from dataclasses import dataclass
from heapq import merge
from typing import AnyStr, List


@dataclass
class ReaderTXT:
    file_txt: str

    def get_line(self) -> List[AnyStr]:
        with open(self.file_txt, 'r') as file:
            return file.readlines()

    def read_txt_into_frozenset(self) -> frozenset:
        result = []
        for line in self.get_line():
            line = line.replace('\n', '')
            result = list(merge(result, line.split(', ')))
        result = frozenset(result)
        return result
