"""
전광판의 숫자
https://www.acmicpc.net/problem/16159
"""

from math import factorial as fac
import sys
input = sys.stdin.readline


class Display:
    char_width = 6
    char_height = 7

    # For identification.
    font = [
        0x312492300, 0x10c104100, 0x782790780, 0x702102700, 0x10c53e100,
        0x79070248c, 0x410792780, 0x782104100, 0x792792780, 0x1e492782082
    ]

    # For print.
    bitmaps = [
        [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]],
        [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]],
        [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],
        [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]],
        [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]],
        [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0]],
        [[0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],
        [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]], [[0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0]]
    ]

    def _parse_single(self, lines_of_row_string: list):
        bin_string = ''.join(lines_of_row_string)
        bits = int(bin_string, base=2)

        if bits not in self.font:
            return -1

        return self.font.index(bits)

    def parse(self, lines_of_row_string: list):
        n_digits = len(lines_of_row_string[0]) // self.char_width
        digits = [[] for _ in range(n_digits)]

        for long_line in lines_of_row_string:
            splited_lines = [long_line[i:i+self.char_width] for i in range(0, len(long_line), self.char_width)]
            for i in range(n_digits):
                digits[i].append(splited_lines[i])

        return [self._parse_single(digit) for digit in digits]

    def print(self, nums: list):
        matrix = [self.bitmaps[num] for num in nums]
        for line in range(self.char_height):
            for digit in range(len(matrix)):
                for column in range(self.char_width):
                    print(matrix[digit][line][column], end='')
            print("")


def next_element(element):
    index_digit_to_swap = -1
    last_digit_value = -1
    for i in range(len(element)-1, -1, -1):
        if element[i] < last_digit_value:
            index_digit_to_swap = i
            break
        last_digit_value = element[i]
    else:
        return None

    min_index = -1
    last_min = 99999
    for i in range(index_digit_to_swap+1, len(element)):
        if element[index_digit_to_swap] < element[i] < last_min:
            min_index = i
            last_min = element[i]

    element[index_digit_to_swap], element[min_index] = element[min_index], element[index_digit_to_swap]

    return element[:index_digit_to_swap+1] + sorted(element[index_digit_to_swap+1:])


if __name__ == "__main__":
    """
    display = Display()
    lines = [input() for _ in range(Display.char_height)]
    parsed = display.parse(lines)
    next = next_element(parsed)
    if next is None:
        print("The End")
    else:
        display.print(next)
    """

    print(next_element([4,2,3,2]))
