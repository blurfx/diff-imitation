from typing import NamedTuple


class DiffResult(NamedTuple):
    flag: int
    old_line_number: int
    new_line_number: int
    text: str
