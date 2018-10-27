# coding=utf-8


class Graph:
    def __init__(self, edges=None):
        self._datas = dict()
        self._edge_count = 0
        if edges is not None:
            for e in edges:
                self.add_edge(e[0], e[1])

    def adj(self, vertex, auto_add=True):
        adjs = self._datas.get(vertex)
        if adjs is None and auto_add:
            adjs = []
            self._datas[vertex] = adjs
        return adjs

    def add_edge(self, vertex1, vertex2):
        adjs1 = self.adj(vertex1)
        adjs1.append(vertex2)
        adjs2 = self.adj(vertex2)
        adjs2.append(vertex1)
        self._edge_count += 1

    def degree(self, vertex):
        adjs = self._datas.get(vertex)
        if adjs is None:
            raise Exception('vertex:' + str(vertex) + 'doesnt exist')
        return len(adjs)

    def V(self):
        return len(self._datas)

    def E(self):
        return self._edge_count

    def vertexes(self):
        return self._datas.keys()
