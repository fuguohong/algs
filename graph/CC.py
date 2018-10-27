# coding=utf-8

from graph.Graph import Graph
import queue


class CC:
    """
    图的连通分量
    """

    def __init__(self, graph: Graph):
        self._graph = graph
        self._count = 0
        self._id = dict()
        self._marked = dict()
        for v in self._graph.vertexes():
            if self._marked.get(v) is not True:
                self._count += 1
                self._search(v)

    def _search(self, start):
        q = queue.Queue()
        q.put(start)
        self._marked[start] = True
        self._id[start] = self._count
        while not q.empty():
            vertex = q.get()
            for v in self._graph.adj(vertex):
                if self._marked.get(v) is not True:
                    q.put(v)
                    self._marked[v] = True
                    self._id[v] = self._count

    def is_connect(self, vertex1, vertex2):
        return self._id[vertex1] == self._id[vertex2]

    def CC_count(self):
        return self._count


# ================= test ===============
if __name__ == '__main__':

    with open('./tinyG.txt') as f:
        g = Graph()
        f.readline()
        f.readline()
        for l in f.readlines():
            datas = l.split(' ')
            g.add_edge(int(datas[0]), int(datas[1]))
        s = CC(g)
        print(s.CC_count())
        print(s.is_connect(2, 6))
