# coding=utf-8

"""
alg-1 p378
强连通性kosaraju算法
"""

from graph.Digraph import Digraph
from graph.DFO import DFO


class SCC:

    def __init__(self, digraph: Digraph):
        if not isinstance(digraph, Digraph):
            raise TypeError('argument must be graph.Digraph')
        self._digraph = digraph
        self._count = 0
        self._sccid = dict()  # 顶点对应的强连通分量id
        self._marked = set()
        order = DFO(digraph.reverse()).postorder()  # 反向图的逆后序顺序进行深度优先遍历
        order.reverse()
        for v in order:
            if v not in self._marked:
                self._search(v)
                self._count += 1
        del self._marked

    def _search(self, vertex):
        self._marked.add(vertex)
        self._sccid[vertex] = self._count
        for v in self._digraph.adj(vertex):
            if v not in self._marked:
                self._search(v)

    def is_scc(self, v1, v2):
        return self._sccid[v1] == self._sccid[v2]

    def scc_count(self):
        return self._count


# ================= test ===============
if __name__ == '__main__':

    with open('./tinyDG.txt') as f:
        g = Digraph()
        f.readline()
        f.readline()
        for l in f.readlines():
            datas = l.strip().split()
            g.add_edge(int(datas[0]), int(datas[1]))
        c = SCC(g)
        print(c.scc_count())
