# 11399번: ATM
# https://www.acmicpc.net/problem/11399

import sys; input = sys.stdin.readline

input()
durations = sorted(list(map(int, input().split())))

total = 0
current = 0
for d in durations:
    current += d
    total += current

print(total)
