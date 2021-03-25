# 1260번: DFS와 BFS
# https://www.acmicpc.net/problem/1260

import sys; input = sys.stdin.readline
from dataclasses import dataclass
from collections import deque
from typing import List


@dataclass(eq=True)
class Node:
    key: int
    neighbors: List['Node']
    visited: bool


class Graph:
    nodes: List[Node]

    def __init__(self, number_of_vertexes):
        self.nodes = [Node(key=i, neighbors=[], visited=False) for i in range(1, number_of_vertexes+1)]

    def connect(self, one_key: int, another_key: int):
        one = self.get_node_by_key(one_key)
        another = self.get_node_by_key(another_key)

        one.neighbors.append(another)
        another.neighbors.append(one)

    def dfs(self, start_key: int):
        self.revoke_visit()
        self._dfs_recursive(self.get_node_by_key(start_key))
        print()

    def _dfs_recursive(self, node: Node):
        node.visited = True
        print(node.key, end=' ')

        for next_node in sorted(node.neighbors, key=lambda _node: _node.key):
            if not next_node.visited:
                self._dfs_recursive(next_node)

    def bfs(self, start_key: int):
        self.revoke_visit()
        self._bfs(self.get_node_by_key(start_key))
        print()

    def _bfs(self, node: Node):
        node.visited = True

        queue = deque([node])

        while queue:
            node = queue.popleft()
            print(node.key, end=' ')

            for next_node in sorted(node.neighbors, key=lambda _node: _node.key):
                if not next_node.visited:
                    queue.append(next_node)
                    next_node.visited = True

    def revoke_visit(self):
        for node in self.nodes:
            node.visited = False

    def get_node_by_key(self, key: int):
        return self.nodes[key - 1]


if __name__ == '__main__':
    n, m, v = map(int, input().split())

    graph = Graph(n)

    for _ in range(m):
        graph.connect(*map(int, input().split()))

    graph.dfs(v)
    graph.bfs(v)
