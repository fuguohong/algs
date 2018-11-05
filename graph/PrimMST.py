# coding=utf-8

from collection.Heap import Heap


def compare(a, b):
    if a.weight < b.weight:
        return 1
    elif a.weight > b.weight:
        return -1
    else:
        return 0


class PrimMST:
    def __init__(self, weighted_grapgh):
        self._weight = 0
        self._edges = []
        self._marked = set()
        self._edges_pq = Heap(compare)
        self._start = next(iter(weighted_grapgh.vertexes()))
        self._visit(weighted_grapgh, self._start)
        while not self._edges_pq.is_empty():
            e = self._edges_pq.pop()
            if e.v1 in self._marked:
                if e.v2 in self._marked:  # 两个顶点都被访问过了，这是一条无效的边
                    continue
                self._visit(weighted_grapgh, e.v2)
            else:
                self._visit(weighted_grapgh, e.v1)
            self._edges.append(e)  # 把权值最小的边加入到最小生成树中
            self._weight += e.weight
        del self._marked
        del self._edges_pq

    def edges(self):
        return self._edges

    def weight(self):
        return self._weight

    def _visit(self, grapg, vertex):
        self._marked.add(vertex)
        for e in grapg.adj(vertex):
            if e.other(vertex) not in self._marked:  # 另一个顶点还没有被访问，将这条边加入到优先队列中
                self._edges_pq.insert(e)


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
        c = PrimMST(g)
        print(time.time() - start)
        print(c.weight())
