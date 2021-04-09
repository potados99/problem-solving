# 11279번: 최대 힙
# https://www.acmicpc.net/problem/11279

import sys; input = sys.stdin.readline
import heapq

# 라이브러리가 주는 힙은 min 힙입니다.
# Max 힙으로 써 봅시다.


def heappush(heap: list, number: int) -> None:
    heapq.heappush(heap, (-number, number))


def heappop(heap: list) -> int:
    if not heap:
        return 0

    return heapq.heappop(heap)[1]


class Executor:
    def __init__(self):
        self.heap = []

    def execute(self, command: int):
        if command == 0:
            self._pop_and_print()
        else:
            self._push(command)

    def _pop_and_print(self):
        print(heappop(self.heap))

    def _push(self, number: int):
        heappush(self.heap, number)


if __name__ == "__main__":
    executor = Executor()

    n = int(input())
    for _ in range(n):
        executor.execute(int(input()))
