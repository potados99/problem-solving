# 14681번: 사분면 고르기
# https://www.acmicpc.net/problem/14681

"""
생각:
    x가 양수면, 1 아님 4
    x가 음수면, 2 아님 3

    y가 양수면, 1 아님 2
    y가 음수면, 3 아님 4

    즉, x가 양수이면 {1, 4}이고, y가 양수이면 {1, 2}인데 이 둘의 교집합은 {1}이다.
    x가 음수이면 {2, 3} y가 양수이면 {1, 2}로, 이 둘의 교집합은 {2}이다.

구현:
    각 차원에 대해 0보다 큰지(1) 작은지(0) 여부를 구해 이로부터 가능한 사분면을 원소로 가지는 집합을 구한다.
    예를 들어 x의 입력이 양수인지는 int(int(input()) > 0) 이라는 식으로 알 수 있다.

    이를 인덱스로 하여 접근할 수 있는 [{2, 3}, {1, 4}] 와 같은 리스트를 준비한다면,
    [{2, 3}, {1, 4}][int(int(input()) > 0)] 와 같은 식으로 x 입력에 따라
    {1, 4}(양수인 경우) 또는 {2, 3}(음수인 경우)를 구할 수 있다.

    같은 방식으로 y의 가능한 사분면 집합을 구한 후, 아까 구한 x의 그것과 교집한 연산을 취해 준다.
    결과는 무조건 원소가 하나인 집합으로 나오게 된다. 여기서 pop 한 값을 출력한다.
"""

print(([{2, 3}, {1, 4}][int(int(input()) > 0)] & [{3, 4}, {1, 2}][int(int(input()) > 0)]).pop())