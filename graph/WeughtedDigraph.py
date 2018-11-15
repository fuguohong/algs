# coding=utf-8

from graph.WeightedGraph import WeightedGraph, WeightedEdge


class WeightedDigraph(WeightedGraph):

    def add_edge(self, v1, v2, weight):
        e = WeightedEdge(v1, v2, weight)
        self._adj(v1).append(e)
        self._adj(v2)
        self._edge_count += 1
