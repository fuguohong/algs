# coding=utf-8

from graph.Graph import Graph

"""
p351
二分图
设G=(V,E)是一个无向图，如果顶点V可分割为两个互不相交的子集(A,B)，
并且图中的每条边（i，j）所关联的两个顶点i和j分别属于这两个不同的顶点集(i in A,j in B)，则称图G为一个二分图。
二分图一定不含有奇数边的环
"""


class TwoColor:
    def __init__(self, graph: Graph):
        self._graph = graph
        self._colors = dict()
        self._marked = dict()
        self._flage = True
        for v in graph.vertexes():
            if self._marked.get(v) is not True:
                self._colors[v] = True
                self._search(v)

    def _search(self, vertex):
        self._marked[vertex] = True
        for v in self._graph.adj(vertex):
            if self._marked.get(v) is not True:
                self._colors[v] = not self._colors[vertex]
                self._search(v)
            elif self._colors[vertex] == self._colors[v]:
                self._flage = False

    def is_two_color(self):
        return self._flage


if __name__ == '__main__':
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(4, 3)
    g.add_edge(4, 1)
    c = TwoColor(g)
    print(c.is_two_color())
