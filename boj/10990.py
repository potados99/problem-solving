# 10990번: 별 찍기 - 15
# https://www.acmicpc.net/problem/10990

import sys; input = sys.stdin.readline


def print_star_tree(n: int):
    center_offset = n - 1

    for i in range(n):
        line = '*' + ' '*(2*i - 1) + '*' if i != 0 else '*'
        print(' '*(center_offset-i) + line)


print_star_tree(int(input()))
