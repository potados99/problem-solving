N, M, K = list(map(lambda x: int(x), input().split(' ')))

distances = []

# Per person
acc_distances = []
tries = []

for i in range(0, N):
    distances.append(list(map(lambda x: int(x), input().split(' '))))
    tries.append(0)
    acc_distances.append(0)

out = False
for j in range(0, M):
    if out:
        break

    for i in range(0, N):
        acc_distances[i] += distances[i][j]
        tries[i] += 1
        if acc_distances[i] >= K:
            print("{i} {tries}".format(i=i+1, tries=tries[i]))

            out = True
            break
