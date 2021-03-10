# 1181번: 단어 정렬
# https://www.acmicpc.net/problem/1181

# 길이 짧은 순, 사전순으로 정렬

import sys; input = sys.stdin.readline
from functools import cmp_to_key


def compare(s1, s2):
    if len(s1) == len(s2):
        return 1 if s1 > s2 else -1
    else:
        return len(s1) - len(s2)


n = int(input())
words = sorted(list(set([input().rstrip() for _ in range(n)])), key=cmp_to_key(compare))

[print(word) for word in words]
