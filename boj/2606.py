# 2606 바이러스
# https://www.acmicpc.net/problem/2606


class Node:
    def __init__(self, key):
        self.key = key
        self.adjacent = []
        self.visited = False


class Graph:
    def __init__(self):
        self.nodes = {}

    def _get_or_create_node(self, key: int):
        if key not in self.nodes:
            self.nodes[key] = Node(key)

        return self.nodes[key]

    def _connect_nodes(self, node1: Node, node2: Node):
        node1.adjacent.append(node2)
        node2.adjacent.append(node1)

    def create_and_connect_nodes_by_key(self, node_key1: int, node_key2: int):
        node1 = self._get_or_create_node(node_key1)
        node2 = self._get_or_create_node(node_key2)

        self._connect_nodes(node1, node2)

    def _search_dfs(self, node: Node):
        for adj in node.adjacent:
            if adj.visits:
                continue
            adj.visits = True

            self._search_dfs(adj)

    def search_dfs(self, start_node_key: int):
        start_node = self.nodes[start_node_key]
        self._search_dfs(start_node)

        # 시작 노드를 제외하고, 이미 방문된 노드의 갯수를 구합니다.
        return list(map(lambda node: node.key != start_node_key and node.visits, self.nodes.values())).count(True)


g = Graph()

number_of_nodes = int(input())
number_of_edges = int(input())

for i in range(number_of_edges):
    (key1, key2) = map(lambda x: int(x), input().split(' '))
    g.create_and_connect_nodes_by_key(key1, key2)

print(g.search_dfs(1))
