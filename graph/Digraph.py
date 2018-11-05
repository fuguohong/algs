# coding=utf-8

from graph.Graph import Graph


class Digraph(Graph):

    # def __init__(self):
    #     Graph.__init__(self)
    #     self._reverse_graph = None

    def add_edge(self, fromv, tov):
        self.adj(fromv).append(tov)
        self._edge_count += 1
        self.adj(tov)  # 如果to没有在顶点中，自动添加to

    def reverse(self):
        g = Digraph()
        for v in self.vertexes():
            for a in self.adj(v):
                g.add_edge(a, v)
        return g

    # def reverse(self):
    #     if self._reverse_graph is None:
    #         for v in self.vertexes():
    #             for a in self.adj(v):
    #                 self._reverse_graph.add_edge(a, v)
    #     return self._reverse_graph
