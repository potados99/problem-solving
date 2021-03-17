# 2163번: 초콜릿 자르기
# https://www.acmicpc.net/problem/2163

import sys; input = sys.stdin.readline

n, m = map(int, input().split())

print((n-1) + n*(m-1))
