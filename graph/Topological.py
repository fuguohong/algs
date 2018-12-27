# coding=utf-8

from graph.Digraph import Digraph
from graph.DFO import DFO
from graph.DirectedCycle import DirectedCycle


class Topological:
    """
    有向图的拓扑排序。有向图必须是无环的，其拓扑排序就是深度优先搜索的逆后序
    时间复杂度O(n) n=V+E
    """

    def __init__(self, digraph):
        self._digraph = digraph
        dc = DirectedCycle(digraph)
        if dc.has_cycle():
            print(dc.cycle())
            raise Exception('topological sort error,digraph has cycle')
        postorder = DFO(digraph).postorder()
        postorder.reverse()
        self._order = postorder

    def order(self):
        return self._order


# ================= test ===============
if __name__ == '__main__':

    with open('./topo.txt', encoding='utf-8') as f:
        g = Digraph()
        for l in f.readlines():
            datas = l.strip().split(' ')
            g.add_edge(datas[0], datas[1])
        c = Topological(g.reverse())
        print(c.order())
