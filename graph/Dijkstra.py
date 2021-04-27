# coding=utf-8

from graph.WeightedDigraph import WeightedDigraph
from collection.IndexedMaxHeap import IndexedMaxHeap


class Dijkstra:
    """
    alg-1 p421
    及时版Dijkstra有向图最短路径算法，不能处理含有负权重的图
    该算法也适用于无向图w = e.v2，改为w = e.other(v) 即可
    时间复杂度 O(ElogV)
    """

    def __init__(self, weighted_digraph: WeightedDigraph, start):
        self.__g = weighted_digraph
        self.__pq = IndexedMaxHeap()
        self._dist_to = dict()
        self._edge_to = dict()
        self._start = start
        # 优先队列。保存了顶点到起点的距离。
        self.__pq.insert(start, 0)
        self._dist_to[start] = 0
        while not self.__pq.is_empty():
            self._relax(self.__pq.pop())
        # 释放引用
        del self.__g
        del self.__pq

    def _relax(self, v):
        vdist = self._dist_to[v]
        for e in self.__g.adj(v):
            w = e.v2
            # 还没有访问这个顶点
            if w not in self._dist_to:
                # 由于是大顶堆，每次要取出离起点最近的点，所以距离取负数
                self.__pq.insert(w, -vdist - e.weight)
                self._edge_to[w] = e
                self._dist_to[w] = vdist + e.weight
                # 这里的小于，对应着距离大于 vdist+weight
            elif self._dist_to[w] > vdist + e.weight:
                self.__pq.update(w, -vdist - e.weight)
                self._edge_to[w] = e
                self._dist_to[w] = vdist + e.weight

    def dist_to(self, v):
        return self._dist_to.get(v)

    def path_to(self, v):
        if v not in self._edge_to:
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
        c = Dijkstra(g, 6)
        for e in c.path_to(7):
            print(e)
