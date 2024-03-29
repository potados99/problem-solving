# 4963번: 섬의 개수
# https://www.acmicpc.net/problem/4963

import sys; input = sys.stdin.readline
from typing import List
from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Position:
    x: int
    y: int


@dataclass()
class Cell:
    is_land: bool
    marked: bool


class World:
    def __init__(self, width: int, height: int, world_map: List[List[int]]):
        self.width = width
        self.height = height
        self.map = [[Cell(False, False) for _ in range(height)] for _ in range(width)]
        self.number_of_islands = 0

        for x in range(width):
            for y in range(height):
                self.map[x][y].is_land = (world_map[y][x] == 1)

    def mark_islands(self, position: Position):
        """
        주어진 위치에 육지가 있다면, 연결된 모든 육지를 찾아 표시하고 number_of_islands를 1 증가시킵니다.

        :param position: 주어진 위치.
        :return: 읎음.
        """
        if not self._is_land(position):
            return

        if self._is_already_marked(position):
            return

        stack = [position]

        while stack:
            popped = stack.pop()

            self.map[popped.x][popped.y].marked = True

            next_positions = [
                p for p in self._eight_way_in_map(popped)
                if self._is_land(p) and not self._is_already_marked(p)
            ]

            stack.extend(next_positions)

        self.number_of_islands += 1

    def _eight_way_in_map(self, position: Position):
        dx = [0, -1, -1, -1, 0, 1, 1, 1]
        dy = [1, 1, 0, -1, -1, -1, 0, 1]

        candidates = [Position(position.x+dx[i], position.y+dy[i]) for i in range(8)]

        return [c for c in candidates if self._is_in_map(c)]

    def _is_in_map(self, position: Position):
        return 0 <= position.x < self.width and 0 <= position.y < self.height

    def _is_land(self, position: Position):
        return self._is_in_map(position) and self.map[position.x][position.y].is_land

    def _is_already_marked(self, position: Position):
        return self._is_in_map(position) and self.map[position.x][position.y].marked


def go():
    while True:
        w, h = map(int, input().split())

        if w == 0 and h == 0:
            break

        raw_world_map = [list(map(int, input().split())) for _ in range(h)]

        world = World(w, h, raw_world_map)

        for x in range(w):
            for y in range(h):
                world.mark_islands(Position(x, y))

        print(world.number_of_islands)


if __name__ == '__main__':
    go()
