from typing import NamedTuple

class Token(NamedTuple):
    class_part: str
    value: str
    line: int
    column: int
