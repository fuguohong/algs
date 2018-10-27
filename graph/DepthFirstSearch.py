# coding=utf-8

from graph.Graph import Graph


class DepthFirstSearch:
    """
    深度优先搜索图
    """

    def __init__(self, graph: Graph, start_vertex):
        self._graph = graph
        self._start_vertex = start_vertex
        self._marked = dict()  # 记录顶点是否走过
        self._edge_to = dict()  # 最后经过顶点的点
        self._count = -1  # 与start_vertex连通的顶点数量
        self._search(start_vertex)

    def _search(self, vertex):
        self._count += 1
        self._marked[vertex] = True
        for next_vertex in self._graph.adj(vertex):
            if self._marked.get(next_vertex) is not True:
                self._edge_to[next_vertex] = vertex
                self._search(next_vertex)

    def has_path_to(self, vertex):
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
    from graph.Digraph import Digraph

    with open('./tinyG.txt') as f:
        g = Digraph()
        f.readline()
        f.readline()
        for l in f.readlines():
            datas = l.split(' ')
            g.add_edge(int(datas[0]), int(datas[1]))
        s = DepthFirstSearch(g, 4)
        print(s.path_to(0))
