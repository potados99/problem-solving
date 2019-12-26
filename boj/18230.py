width, n_one, n_two = map(lambda x: int(x), input().split(' '))
one = sorted(map(int, input().split(' ')), reverse=True)
two = sorted(map(int, input().split(' ')), reverse=True)

beauty = 0
# Iterate for bigger one.
for len_two in range(n_two+1):
    len_one = width - (2 * len_two)
    if not 0 <= len_one <= n_one: continue
    beauty = max(beauty, sum(one[:len_one]) + sum(two[:len_two]))

print(beauty)
