import colored

from base_formatter import BaseFormatter


class Added(BaseFormatter):
    def __init__(self, items):
        super().__init__(items)
        self._items = items

    def get_range(self):
        diff_range = f'{colored.fg("cyan")}{self._items[0][1]}a{self._items[0][2]}'
        if len(self._items) > 1:
            diff_range += f",{self._items[-1][2]}"
        return diff_range

    def format(self):
        output = [f'{colored.fg("green")}> {item[3]}' for item in self._items]
        return "\n".join(output)


class Deleted(BaseFormatter):
    def __init__(self, items):
        super().__init__(items)
        self._items = items

    def get_range(self) -> str:
        diff_range = f"{colored.fg('cyan')}{self._items[0][1]}d{self._items[0][2]}"
        if len(self._items) > 1:
            diff_range += f",{self._items[-1][2]}"
        return diff_range

    def format(self) -> str:
        output = [f'{colored.fg("red")}> {item[3]}' for item in self._items]
        return "\n".join(output)


class Updated(BaseFormatter):
    def __init__(self, items):
        super().__init__(items)
        self._added_items = [item for item in items if item[0] == 1]
        self._added_formatter = Added(self._added_items)

        self._deleted_items = [item for item in items if item[0] == 0]
        self._deleted_formatter = Deleted(self._deleted_items)

    def get_range(self) -> str:
        diff_range = f"{colored.fg('cyan')}{self._deleted_items[0][1]}"
        if len(self._deleted_items) > 1:
            diff_range += f",{self._deleted_items[-1][1]}"

        diff_range += f"c{self._added_items[0][2]}"
        if len(self._added_items) > 1:
            diff_range += f",{self._added_items[-1][2]}"
        return diff_range

    def format(self) -> str:
        return "\n".join(
            [
                self._deleted_formatter.format(),
                f'{colored.fg("white")}---',
                self._added_formatter.format(),
            ]
        )
