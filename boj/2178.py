# 2178번: 미로 탐색
# https://www.acmicpc.net/problem/2178

import sys; input = sys.stdin.readline
from collections import deque


def four_way(c: tuple):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    return [(c[0] + dx[i], c[1] + dy[i]) for i in range(4)]


def in_map(c: tuple, map_size: tuple):
    return 0 <= c[0] < map_size[0] and 0 <= c[1] < map_size[1]


n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

queue = deque()

visited[0][0] = True
queue.append((0, 0, 1))

while queue:
    x, y, count = queue.popleft()

    if (x, y) == (n-1, m-1):
        print(count)

    for x, y in four_way((x, y)):
        if not in_map((x, y), (n, m)):
            continue

        if maze[x][y] == 0:
            continue

        if visited[x][y]:
            continue

        visited[x][y] = True

        queue.append((x, y, count+1))
