# 10809번: 알파벳 찾기
# https://www.acmicpc.net/problem/10809

import sys; input = sys.stdin.readline


def index(string: str, substring: str):
    try:
        return string.index(substring)
    except ValueError:
        return -1


word = input()

print(' '.join([str(index(word, chr(ascii_value))) for ascii_value in range(97, 122+1)]))
