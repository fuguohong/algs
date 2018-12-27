# coding=utf-8

from collection.Heap import Heap
from graph.WeightedGraph import WeightedGraph


def compare(a, b):
    if a.weight < b.weight:
        return 1
    elif a.weight > b.weight:
        return -1
    else:
        return 0


class LazyDijkstra:
    """
    alg4 p421
    延时版Dijkstra有向图最短路径算法，不能处理含有负权重的图
    时间复杂度 O(ElogE)
    """

    def __init__(self, weighted_grapgh: WeightedGraph, start):
        self.__g = weighted_grapgh
        self.__marked = set()
        self.__pq = Heap(compare)
        self._dist_to = dict()
        self._edge_to = dict()
        self._start = start
        # 初始化达达起点的权重为0
        self._dist_to[start] = 0
        # 首先访问一次起点
        self._relax(start)
        while not self.__pq.is_empty():
            e = self.__pq.pop()
            # 边到达的顶点没有访问过，就访问这个顶点（起点一定被访问过，否则边不会存在在队列中）。
            if e.v2 not in self.__marked:
                self._relax(e.v2)
        # 释放引用
        del self.__g
        del self.__marked
        del self.__pq

    def _relax(self, v):
        # 将顶点标记访问
        self.__marked.add(v)
        for e in self.__g.adj(v):
            # 走e权重小，就更换到达顶点的边为e
            if e.v2 not in self._dist_to or self._dist_to.get(e.v2) > self._dist_to[v] + e.weight:
                self._edge_to[e.v2] = e
                self._dist_to[e.v2] = self._dist_to[v] + e.weight
                self.__pq.insert(e)

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


# TODO 及时版dijkstra算法； 无向图最短路径算法； 负权重最短路径即负环检测
# ================== test ===============
if __name__ == '__main__':
    with open('./tinyWG.txt') as f:
        g = WeightedGraph()
        for l in f.readlines():
            datas = l.split(' ')
            g.add_edge(int(datas[0]), int(datas[1]), float(datas[2]))
        c = LazyDijkstra(g, 3)
        print(c.path_to(7))
