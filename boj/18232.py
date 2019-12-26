import sys
input = sys.stdin.readline

N, M = map(lambda x: int(x), input().split(' '))
S, E = map(lambda x: int(x), input().split(' '))
neighbers = [[] for x in range(0, N+1)]
for i in range(0, M):
    p1, p2 = map(lambda x: int(x), input().split(' '))
    neighbers[p1].append(p2)
    neighbers[p2].append(p1)

q = list()
q.append(S)
front = 0

dist = [None for x in range(0, N + 1)]
dist[S] = 0

while dist[E] == None:
    current = q[front]
    front += 1

    if current + 1 <= N and dist[current + 1] == None:
        dist[current + 1] = dist[current] + 1
        q.append(current + 1)

    if current - 1 >= 1 and dist[current - 1] == None:
        dist[current - 1] = dist[current] + 1
        q.append(current - 1)

    for neighber in neighbers[current]:
        if dist[neighber] == None:
            dist[neighber] = dist[current] + 1
            q.append(neighber)

print(dist[E])
