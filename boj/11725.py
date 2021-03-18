# 11725번: 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

import sys; input = sys.stdin.readline
from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    id: int
    neighbors: list
    visited: bool = False


class Tree:
    def __init__(self):
        self.nodes: List[Node] = []

    def create_nodes(self, how_many: int):
        """
        노드를 1 ~ how_many까지 how_many개 생성합니다.

        :param how_many: 몇개.
        :return: 읎음.
        """
        self.nodes = [Node(node_id, []) for node_id in range(1, how_many + 1)]

    def connect_nodes(self, one_id: int, another_id: int):
        """
        두 노드 이어줍니다.
        양쪽 모두에 연결이 생깁니다.

        :param one_id: 한 노드의 id.
        :param another_id: 다른 노드의 id.
        :return: 읎음.
        """
        one_node = self.get_node(one_id)
        another_node = self.get_node(another_id)

        one_node.neighbors.append(another_node)
        another_node.neighbors.append(one_node)

    def iterate_all_nodes_and_build_child_to_parent_dictionary(self, root_node_id: int):
        """
        모든 노드를 돌아다니면서 부모-자식 관계를 찾습니다.
        깊이 우선 탐색 비슷하게 갑니다.

        :param root_node_id: 루트 노드의 id.
        :return: 완성된 부모-자식 관계 딕셔너리. {자식 노드 id: 부모 노드 id} 형식.
        """
        stack = [self.get_node(root_node_id)]
        child_to_parent = {}

        while stack:
            parent = stack.pop()

            for child in parent.neighbors:
                # 여기 방문 가능?
                if child.visited:
                    continue

                # 삽가능
                child_to_parent[child.id] = parent.id

                # 이제부터 불가능
                child.visited = True

                stack.append(child)

        return child_to_parent

    def get_node(self, node_id: int):
        """
        node_id를 id로 가지는 노드를 가져옵니다.

        왜 이게 필요하냐면... 노드는 0번지부터 저장되구, 노드 id는 1부터 시작하기 때문입니다.
        바꿀 생각 없음!

        :param node_id: 노드 id
        :return: 노드
        """
        return self.nodes[node_id - 1]


if __name__ == '__main__':
    n = int(input())

    tree = Tree()
    tree.create_nodes(n)

    # 입력받고 노드 연결
    for _ in range(n - 1):
        one, another = map(int, input().split())
        tree.connect_nodes(one, another)

    # 트리 순회하며 '자식 to 부모' 딕셔너리 완성
    parents = tree.iterate_all_nodes_and_build_child_to_parent_dictionary(root_node_id=1)

    # '자식 to 부모' 관계 차례대로 출력
    for i in range(2, n + 1):
        print(parents[i])
