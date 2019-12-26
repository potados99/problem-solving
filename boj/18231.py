N, M = map(lambda x: int(x), input().split(' '))
neighbers = [[] for x in range(0, N+1)]
for i in range(0, M):
    city1, city2 = map(lambda x: int(x), input().split(' '))
    neighbers[city1].append(city2)
    neighbers[city2].append(city1)
n_destroyed = int(input())
destroyed = set(map(lambda x: int(x), input().split(' ')))

# Get bombed cities.
cities = set(range(1, N+1))
not_destroyed = cities - destroyed

bombed = set(destroyed) # Assume all destroyed cities are bombed.
for city in not_destroyed:
    bombed -= set(neighbers[city]) # Remove not actually bombed cities.

# Check validity.
should_have_been_destroyed = set()
for city in bombed:
    should_have_been_destroyed |= set(neighbers[city]) | {city}

if len(destroyed - should_have_been_destroyed) != 0:
    bombed.clear()

if len(bombed) == 0:
    print(-1)
else:
    print(len(bombed))
    for city in sorted(list(bombed)):
        print(city, end=' ')
