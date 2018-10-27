# coding=utf-8

"""
p362
边的连通性，图中是否含有桥（删除该边后，图分为两个独立连通分量）
"""

from graph.Graph import Graph


class Brige:
    def __init__(self, graph: Graph):
        """
        :param graph: 连通图
        """
        self._graph = graph
        self._briges = []
        self._current = 0
        self._order = dict()  # 记录遍历顺序
        self._low = dict()  # 通过非前导路径能够回到的最小父顶点
        self.start = next(iter(graph.vertexes()))
        self._search(self.start, self.start)

    def _search(self, pre, current):
        self._order[current] = self._current
        self._low[current] = self._current
        self._current += 1
        for nextv in self._graph.adj(current):
            if self._order.get(nextv) is None:
                self._search(current, nextv)
                self._low[current] = min(self._low[current], self._low[nextv])
                if self._low[current] == self._order[current] and current != self.start:
                    self._briges.append((pre, current))
            elif nextv != pre:  # 不是来的路径
                self._low[current] = min(self._low[nextv], self._order[current])

    def has_brige(self):
        return len(self._briges) == 0

    def briges(self):
        return self._briges


# ================= test ===============
if __name__ == '__main__':
    g = Graph()
    g.add_edge(1, 3)
    # g.add_edge(1, 2)
    # g.add_edge(1, 6)
    # g.add_edge(4, 3)
    # g.add_edge(2, 6)
    # g.add_edge(9, 10)
    # g.add_edge(6, 10)
    s = Brige(g)
    print(s.briges())
