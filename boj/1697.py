# 1697번: 숨바꼭질
# https://www.acmicpc.net/problem/1697

import sys; input = sys.stdin.readline
from collections import deque


start, dest = map(int, input().split())
visited = [False] * 200_001

queue = deque()

visited[start] = True
queue.append((start, 0))

while queue:
    position, count = queue.popleft()

    if position == dest:
        print(count)

    for d in [position-1, position+1, position*2]:
        if 0 <= d <= 200_000 and not visited[d]:
            queue.append((d, count+1))
            visited[d] = True
