# 1012번: 유기농 배추
# https://www.acmicpc.net/problem/1012

import sys; input = sys.stdin.readline
from typing import List, Callable
from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Position:
    x: int
    y: int


@dataclass()
class Cell:
    has_cabbage: bool
    marked: bool


class Ground:
    def __init__(self, width: int, height: int, cabbage_positions: List[Position]):
        self.width = width
        self.height = height
        self.map = [[Cell(False, False) for _ in range(height)] for _ in range(width)]
        self.number_of_groups = 0

        for p in cabbage_positions:
            self.map[p.x][p.y].has_cabbage = True

    def mark_adjacents(self, position: Position):
        if not self._has_cabbage_here(position):
            return

        if self._already_marked_here(position):
            return

        stack = [position]
        newly_marked = False

        while stack:
            popped = stack.pop()
            self.map[popped.x][popped.y].marked = True
            newly_marked = True

            next_positions = [
                p for p in self._four_way_available(popped)
                if self._has_cabbage_here(p) and not self._already_marked_here(p)
            ]

            stack.extend(next_positions)

        if newly_marked:
            self.number_of_groups += 1

    def _four_way_available(self, position: Position):
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        candidates = [Position(position.x+dx[i], position.y+dy[i]) for i in range(4)]

        return [c for c in candidates if self._in_map(c)]

    def _has_cabbage_here(self, position: Position):
        return self._in_map(position) and self.map[position.x][position.y].has_cabbage

    def _already_marked_here(self, position: Position):
        return self.map[position.x][position.y].marked

    def _in_map(self, position: Position):
        return 0 <= position.x < self.width and 0 <= position.y < self.height


if __name__ == '__main__':
    number_of_cases = int(input())
    for _ in range(number_of_cases):
        w, h, n = map(int, input().split())

        positions = [Position(coordinate[0], coordinate[1]) for coordinate in [list(map(int, input().split())) for _ in range(n)]]
        ground = Ground(w, h, positions)

        for x in range(w):
            for y in range(h):
                ground.mark_adjacents(Position(x, y))

        print(ground.number_of_groups)

