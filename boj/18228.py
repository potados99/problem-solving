number_of_ices = int(input())
ice_thresholds = list(map(lambda x: int(x), input().split(' ')))
penguin_index = ice_thresholds.index(-1)

min_left = min(ice_thresholds[0:penguin_index])
min_right = min(ice_thresholds[penguin_index+1:])

print(min_left + min_right)
