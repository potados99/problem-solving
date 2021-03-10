# 8958번: OX퀴즈
# https://www.acmicpc.net/problem/8958

import sys; input = sys.stdin.readline

n = int(input())
cases = [input() for _ in range(n)]

for case in cases:

    score_total = 0
    combo = 0

    for result in case:
        if result == 'O':
            combo += 1
            score_total += combo
        else:
            combo = 0

    print(score_total)
