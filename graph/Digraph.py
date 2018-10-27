# coding=utf-8

from graph.Graph import Graph


class Digraph(Graph):

    def add_edge(self, fromv, tov):
        self.adj(fromv).append(tov)
        self._edge_count += 1
        self.adj(tov)  # 如果to没有在顶点中，自动添加to
