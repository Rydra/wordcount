from dataclasses import dataclass
from typing import List, Dict, Tuple


@dataclass
class Frequence:
    word: str
    line_appearances: List[int]
    num_appearances: int

    def add_appearance(self, num_line, num_appearances):
        self.line_appearances.append(num_line)
        self.num_appearances += num_appearances


def most_frequent_words(file_path: str, top_n: int = 5) -> List[Frequence]:
    # TODO: Your implementation here
    return []
