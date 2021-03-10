# 11720번: 숫자의 합
# https://www.acmicpc.net/problem/11720

import sys; input = sys.stdin.readline

input()
number_string = input().rstrip()

total = 0
for digit in number_string:
    total += int(digit)

print(total)
