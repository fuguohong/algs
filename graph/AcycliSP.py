# coding=utf-8

from graph.Topological import Topological
from graph.WeightedDigraph import WeightedDigraph


class AcycliSP:
    """
    alg4 p425
    有向无环图最路径。根据它的拓扑排序放松边即可得到最短（长）路径
    时间复杂度O(n) n=E+V
    该算法可以解决 优先级限制下的并行任务调度问题 alg4 p429
    """

    def __init__(self, digraph: WeightedDigraph):
        topo_order = Topological(digraph).order()
        self.__g = digraph
        self.__dist_to = dict()
        self._edge_to = dict()

        self.__dist_to[topo_order[0]] = 0
        for v in topo_order:
            self._relax(v)
        del self.__g
        del self.__dist_to

    def _relax(self, v):
        for e in self.__g.adj(v):
            if e.v2 not in self.__dist_to or self.__dist_to[e.v2] > self.__dist_to[e.v1] + e.weight:
                self._edge_to[e.v2] = e
                self.__dist_to[e.v2] = self.__dist_to[e.v1] + e.weight

    def path(self, start, end):
        """
        从start到end的最短路径
        :param start: 顶点
        :param end: 顶点
        :return: list[WeightedEdge] or None
        """
        if end not in self._edge_to:
            return None
        e = self._edge_to[end]
        edges = []
        while True:
            edges.append(e)
            if e.v1 == start:
                break
            e = self._edge_to.get(e.v1)
            if e is None:
                return None
        edges.reverse()
        return edges
