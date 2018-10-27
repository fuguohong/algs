# coding=utf-8

from graph.Graph import Graph
import queue


class BreadFirstSearch:
    """
    广度优先搜索图
    """
    def __init__(self, graph: Graph, start_vertex):
        self._graph = graph
        self._start_vertex = start_vertex
        self._marked = dict()  # 记录顶点是否走过
        self._edge_to = dict()  # 最短路径
        self._count = 0  # 与start_vertex连通的顶点数量
        self._search()

    def _search(self):
        q = queue.Queue()
        self._marked[self._start_vertex] = True
        self._edge_to[self._start_vertex] = self._start_vertex
        q.put(self._start_vertex)
        while not q.empty():
            vertex = q.get()
            for v in self._graph.adj(vertex):
                if self._marked.get(v) is not True:
                    self._count += 1
                    q.put(v)
                    self._marked[v] = True
                    self._edge_to[v] = vertex  # 广度优先，最先到达点的一定是深度最小的

    def is_connect(self, vertex):
        return self._marked.get(vertex) is True

    def vertext_count(self):
        return self._count

    def path_to(self, vertex):
        pre_vertex = self._edge_to.get(vertex)
        if pre_vertex is None:
            return None
        path = [vertex]
        while pre_vertex != self._start_vertex:
            path.append(pre_vertex)
            pre_vertex = self._edge_to[pre_vertex]
        path.append(self._start_vertex)
        path.reverse()
        return path


# ================= test ===============
if __name__ == '__main__':

    with open('./tinyG.txt') as f:
        g = Graph()
        f.readline()
        f.readline()
        for l in f.readlines():
            datas = l.split(' ')
            g.add_edge(int(datas[0]), int(datas[1]))
        s = BreadFirstSearch(g, 2)
        print(s.vertext_count())
        print(s.path_to(4))
