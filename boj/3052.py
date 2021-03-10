# 3052번: 나머지
# https://www.acmicpc.net/problem/3052

import sys; input = sys.stdin.readline

numbers = [int(input()) for _ in range(10)]
lefts = [number % 42 for number in numbers]

print(len(set(lefts)))
