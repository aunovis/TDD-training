from functools import reduce


class StringCalculator(object):
    def __init__(self):
        self._call_count = 0

    def _parse_delimiter(self, numbers: str) -> (str, str):
        if numbers.startswith("//"):
            newline_idx = numbers.find("\n")
            return (numbers[2:newline_idx], numbers[newline_idx + 1:])
        else:
            return (",", numbers)

    @property
    def call_count(self):
        return self._call_count

    def add(self, numbers: str) -> int:
        self._call_count += 1
        if len(numbers) == 0:
            return 0
        delimiter, rest = self._parse_delimiter(numbers)
        parts = rest.replace("\n", delimiter).split(delimiter)
        ints = list(map(int, parts))
        negative_ints = list(filter(lambda x: x < 0, ints))
        if len(negative_ints) > 0:
            raise ValueError(f"negatives not allowed: {' '.join(map(str, negative_ints))}")
        return reduce(int.__add__, ints, 0)
