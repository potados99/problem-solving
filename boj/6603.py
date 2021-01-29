# 6603 로또
# https://www.acmicpc.net/problem/6603

"""
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
"""


def print_every_combination(pool: list, picked_items: list, to_pick: int):
    # nCr 개의 출력이 나올 겁니다.

    # 다 뽑았으면 출력하고 끝냅니다.
    if to_pick == 0:
        print(' '.join(map(lambda x: str(x), picked_items)))
        return

    for item in pool:
        # 이미 장바구니에 넣었으면 넘어가요~
        if item in picked_items:
            continue

        # 오름차순이 안 될 것 같다 싶으면 넘어가요~
        if len(picked_items) > 0 and item < picked_items[len(picked_items) - 1]:
            continue

        # 지금까지 뽑은 아이템 + 지금 뽑은 아이템으로 새 객체를 만들어 다음 레벨로 갑니다.
        print_every_combination(pool, picked_items + [item], to_pick - 1)


def run_test_case(pool):
    print_every_combination(
        pool,        # 전체 중에서
        [],          # 빈 장바구니에
        6            # 몇 개를 담을까요
    )

    print('')


test_inputs = [True]
while test_inputs:
    number_of_inputs, *test_inputs = list(map(lambda x: int(x), input().split(' ')))

    run_test_case(test_inputs)
