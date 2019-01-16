# coding=utf-8


class WeightedEdge:
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def other(self, v):
        if v == self.v1:
            return self.v2
        elif v == self.v2:
            return self.v1
        else:
            raise Exception('v is not a vertex of this edge')

    def __str__(self):
        return '[%s]__%.2f__[%s]' % (self.v1, self.weight, self.v2)


class WeightedGraph:
    def __init__(self):
        self._datas = dict()
        self._edge_count = 0
        self._edges = None

    def add_edge(self, v1, v2, weight):
        e = WeightedEdge(v1, v2, weight)
        self._adj(v1).append(e)
        self._adj(v2).append(e)
        self._edge_count += 1

    def vertexes(self):
        return self._datas.keys()

    def adj(self, v):
        return self._datas.get(v)

    def edges(self):
        if self._edges is None:
            self._edges = set()
        for v in self.vertexes():
            for e in self.adj(v):
                self._edges.add(e)
        return self._edges

    def _adj(self, v):
        a = self._datas.get(v)
        if a is None:
            a = []
            self._datas[v] = a
        return a

    def V(self):
        return len(self._datas)

    def E(self):
        return self._edge_count
