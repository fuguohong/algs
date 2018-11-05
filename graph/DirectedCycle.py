# coding=utf-8

from graph.Digraph import Digraph


class DirectedCycle:
    def __init__(self, digraph: Digraph):
        if not isinstance(digraph, Digraph):
            raise TypeError('argument must be graph.Digraph')
        self._digraph = digraph
        self._marked = set()
        self._current_path = None  # 当前路径经过的顶点
        self._cycle = None
        for v in self._digraph.vertexes():
            if v not in self._marked:
                self._current_path = {v: v}
                self._search(v)
        del self._current_path
        del self._marked

    def _search(self, vertex):
        self._marked.add(vertex)
        for n in self._digraph.adj(vertex):
            if self.has_cycle():
                return
            if n not in self._marked:  # 该点没有经过
                self._current_path[n] = vertex  # 添加到当前路径中
                self._search(n)  # 继续向下
            elif n in self._current_path:  # 该点已经经过， 并且在当前路径中，出现环
                self._cycle = []
                pre = vertex
                while pre != n:  # 原路返回到n点
                    self._cycle.append(pre)
                    pre = self._current_path[pre]
                self._cycle.append(n)
                self._cycle.reverse()  # 因为是返回，所以环的顺序是反的
        del self._current_path[vertex]  # 往回走，从路径中删除

    def cycle(self):
        return self._cycle

    def has_cycle(self):
        return self._cycle is not None


# ================= test ===============
if __name__ == '__main__':

    with open('./tinyDG.txt') as f:
        g = Digraph()
        f.readline()
        f.readline()
        for l in f.readlines():
            datas = l.split('  ')
            g.add_edge(int(datas[0]), int(datas[1]))
        c = DirectedCycle(g)
        print(c.has_cycle())
        print(c.cycle())
