# 2577번: 숫자의 개수
# https://www.acmicpc.net/problem/2577

import sys; input = sys.stdin.readline

a, b, c = [int(input()) for _ in range(3)]
multiplied = a * b * c
digits_in_string = str(multiplied)

for i in range(10):
    print(digits_in_string.count(str(i)))
