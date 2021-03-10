# 1085번: 직사각형에서 탈출
# https://www.acmicpc.net/problem/1085

import sys; input = sys.stdin.readline

x, y, w, h = map(int, input().split())

# 한 방향으로만 움직이는게 이득이다.

# 가로로 탈출하기
horizontal_distance = min(x, w - x)

# 세로로 탈출하기
vertical_distance = min(y, h - y)

# 둘 중 짧은 것
min_distance = min(horizontal_distance, vertical_distance)

print(min_distance)
