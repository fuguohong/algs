# coding=utf-8

from graph.Topological import Topological


class SignlePath:
    """
    汉密尔顿路径：有向图中是否存在一条只访问每个顶点一次的路径
    含有汉密尔顿路径的有向图拥有唯一拓扑排序，否则拥有多种拓扑排序
    """

    def __init__(self, digraph):
        self._digraph = digraph
        topo = Topological(digraph)
        topoder = topo.order()
        self._path = topoder
        for i in range(len(topoder) - 1):
            if topoder[i + 1] not in digraph.adj(topoder[i]):  # 拓扑排序中，每个点都有边到达下一个点
                self._path = None
                break

    def path(self):
        return self._path


if __name__ == '__main__':
    from graph.Digraph import Digraph
    import os

    with open(os.path.abspath('../graph/topo.txt'), encoding='utf-8') as f:
        g = Digraph()
        for l in f.readlines():
            datas = l.strip().split(' ')
            g.add_edge(datas[0], datas[1])
        c = SignlePath(g)
        print(c.path())
