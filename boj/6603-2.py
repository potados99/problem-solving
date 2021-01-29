# 6603 로또
# https://www.acmicpc.net/problem/6603

# https://jun-itworld.tistory.com/15 보고 깊게 감명받아 다시 풀었습니다.

"""
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
"""

# 뽑을 대상이 있는 풀.
pool = []

# 그 풀의 크기.
pool_size = 0

# 풀에서 뽑을 대상의 갯수.
to_pick = 6

# 풀에서 뽑은 대상. 6개만 뽑을 것이므로 6개 준비해둡니다.
picked = [None for _ in range(6)]

# 테스트 입력. Truthy 하도록 아무 값이나 대충 넣어 줍니다.
test_inputs = [True]


def print_every_combination(start: int = 0, depth: int = 0):
    # 다 뽑았으면 출력하고 끝냅니다.
    if depth == to_pick:
        print(*picked)
        return

    for i in range(start, pool_size):
        picked[depth] = pool[i]

        # 지금까지 뽑은 것 다음부터 뽑기 때문에 자연히 중복 없는 오름차순이 됩니다.
        print_every_combination(i + 1, depth + 1)


def run_test_case():
    print_every_combination()

    print('')


while test_inputs:
    number_of_inputs, *test_inputs = list(map(lambda x: int(x), input().split(' ')))

    pool_size = number_of_inputs
    pool = test_inputs

    run_test_case()
