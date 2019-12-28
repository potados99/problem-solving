"""
전광판의 숫자
https://www.acmicpc.net/problem/16159
"""

from math import factorial as fac


class Display:
    char_width = 6
    char_height = 7

    # Font bitmap in hex representation.
    font = [
        0x312492300, 0x10c104100, 0x782790780, 0x702102700, 0x10c53e100,
        0x79070248c, 0x410792780, 0x782104100, 0x792792780, 0x1e492782082
    ]

    def __init__(self):
        self.matrix = [self._get_bit_matrix(num) for num in range(10)]

    def _get_bit_matrix(self, num: int):
        if not (0 <= num <= 9):
            return None

        on_bits = self.font[num]
        rows = []
        for i in range(self.char_height):
            row = []
            for j in range(self.char_width):
                row.insert(0, on_bits & 1)
                on_bits >>= 1

            rows.insert(0, row)

        return rows

    def _parse_single(self, lines_of_row_string: list):
        parsed_matrix = [[int(char) for char in line] for line in lines_of_row_string]

        if parsed_matrix not in self.matrix:
            return -1

        return self.matrix.index(parsed_matrix)

    def parse(self, lines_of_row_string: list):
        n_digits = len(lines_of_row_string[0]) // self.char_width
        digits = [[] for _ in range(n_digits)]

        for long_line in lines_of_row_string:
            splited_lines = [long_line[i:i+self.char_width] for i in range(0, len(long_line), self.char_width)]
            for i in range(n_digits):
                digits[i].append(splited_lines[i])

        return [self._parse_single(digit) for digit in digits]

    def print(self, nums: list):
        matrix = [self._get_bit_matrix(num) for num in nums]

        for line in range(self.char_height):
            for digit in range(len(matrix)):
                for column in range(self.char_width):
                    print(matrix[digit][line][column], end='')
            print("")


def permutation_recursive(data: list, n: int, r: int, results: list):
    if r == 0:
        results.append([x for x in data])

    for i in range(n):
        data[i], data[n-1] = data[n-1], data[i]
        permutation_recursive(data, n-1, r-1, results)
        data[i], data[n-1] = data[n-1], data[i]


def create_permutations(nums: list):
    permutations = []
    permutation_recursive(nums, len(nums), len(nums), permutations)
    return sorted(permutations)


def next_element(element, collection: list):
    if element not in collection:
        return None

    element_index = collection.index(element)

    if element_index == len(collection) - 1:
        # No next. It is the last.
        return None
    else:
        return collection[element_index + 1]


if __name__ == "__main__":
    display = Display()
    lines = [input() for _ in range(Display.char_height)]
    parsed = display.parse(lines)
    permutations = create_permutations(parsed)
    next = next_element(parsed, permutations)
    if next is None:
        print("The End")
    else:
        display.print(next)
