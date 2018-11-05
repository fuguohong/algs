# coding=utf-8

from graph.Digraph import Digraph
from graph.DFO import DFO
from graph.DirectedCycle import DirectedCycle


class Topological:
    def __init__(self, digraph: Digraph):
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
