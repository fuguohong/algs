# coding=utf-8

from graph.UnionFind import UnionFind
from collection.Heap import Heap
from graph.WeightedGraph import WeightedGraph


def compare(a, b):
    if a.weight < b.weight:
        return 1
    elif a.weight > b.weight:
        return -1
    else:
        return 0


class KruskalMST:
    def __init__(self, weightd_graph: WeightedGraph):
        if not isinstance(weightd_graph, WeightedGraph):
            raise TypeError('argument must be graph.WeightedGraph')
        self._edges = []
        self._weight = 0
        # end instance attributes
        edgespq = Heap(compare)  # 小顶堆，保存树的所有边
        uf = UnionFind()
        for e in weightd_graph.edges():
            edgespq.insert(e)
        while not edgespq.is_empty() and len(self._edges) < weightd_graph.V() - 1:
            e = edgespq.pop()
            if uf.is_connected(e.v1, e.v2):  # v1 v2已经连接由更小的边，再加入e会形成环
                continue
            uf.union(e.v1, e.v2)
            self._edges.append(e)
            self._weight += e.weight

    def edges(self):
        return self._edges

    def weight(self):
        return self._weight


# ================== test ===============
if __name__ == '__main__':

    from graph.WeightedGraph import WeightedGraph
    import time

    with open('./10000EWG.txt') as f:
        x = f.readline()
        f.readline()
        g = WeightedGraph()
        for l in f.readlines():
            datas = l.split(' ')
            g.add_edge(int(datas[0]), int(datas[1]), float(datas[2]))
        start = time.time()
        c = KruskalMST(g)
        print(time.time()-start)
        print(c.weight())
