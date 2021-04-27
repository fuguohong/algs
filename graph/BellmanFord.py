# coding=utf-8

from graph.WeightedDigraph import WeightedDigraph
from graph.DirectedCycle import EdgeDirectedCycle
from collections import deque


class BellmanFord:
    """
    alg-1 p433/438
    含有负权重边的有向图最短路径算法。
    如果含有负权重的环，则最短路径没有意义。该算法可以检测图中是否含有负权重环
    时间复杂度，最好情况V+E, 最坏情况VE
    """

    def __init__(self, weighted_digrapg: WeightedDigraph, start):
        self.__g = weighted_digrapg
        self.__pq = deque()
        # 记录顶点是否在队列中，避免重复入队
        self.__onpq = dict()
        # 记录放松的次数，v次放松后查找是否有环
        self.__relax_time = 0
        self._cycle = None
        self._start = start
        self._edge_to = dict()
        self._dist_to = dict()

        self.__pq.append(start)
        self.__onpq[start] = True
        self._dist_to[start] = 0
        while len(self.__pq) != 0 and self._cycle is None:
            v = self.__pq.popleft()
            self.__onpq[v] = False
            self._relax(v)

        del self.__g
        del self.__pq
        del self.__onpq

    def _relax(self, v):
        for e in self.__g.adj(v):
            # 只将引起改变的顶点入队，避免放松不会引起改变的顶点
            if e.v2 not in self._dist_to or self._dist_to[e.v2] > self._dist_to[v] + e.weight:
                self._dist_to[e.v2] = self._dist_to[v] + e.weight
                self._edge_to[e.v2] = e
                if not self.__onpq.get(e.v2):
                    self.__pq.append(e.v2)
                    self.__onpq[e.v2] = True
        self.__relax_time += 1
        if self.__relax_time % self.__g.V() == 0:
            self._find_cycle()

    def _find_cycle(self):
        graph = WeightedDigraph()
        for e in self._edge_to.values():
            graph.add_edge(e.v1, e.v2, e.weight)
        graph_cycle = EdgeDirectedCycle(graph)
        self._cycle = graph_cycle.cycle()

    def has_negativa_cycle(self):
        return self._cycle is not None

    def negativa_cycle(self):
        return self._cycle

    def dist_to(self, v):
        return self._dist_to.get(v)

    def path_to(self, v):
        if v not in self._edge_to:
            return None
        if self.has_negativa_cycle():
            return None
        edges = []
        e = self._edge_to[v]
        while e.v1 != self._start:
            edges.append(e)
            e = self._edge_to[e.v1]
        edges.append(e)
        edges.reverse()
        return edges


# ================== test ===============
if __name__ == '__main__':
    with open('./tinyWG.txt') as f:
        g = WeightedDigraph()
        for l in f.readlines():
            datas = l.split(' ')
            g.add_edge(int(datas[0]), int(datas[1]), float(datas[2]))
        c = BellmanFord(g, 6)
        if c.has_negativa_cycle():
            for e in c.negativa_cycle():
                print(e)
