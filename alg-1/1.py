# coding=utf-8

"""
p 136
动态连通性问题，解决任意两点之间是否连通
"""

"""
采用压缩路径的加权quick-union算法,权为树的size，这样会使树的平均深度最低。经历多次find后，find操作的时间复杂度无限接近于1
"""


class UnionFind:
    def __init__(self):
        # 索引表示node, 值表示该node连接的点
        self._node_union = dict()
        self._tree_size = dict()
        self.union_count = 0

    def find_root(self, node):
        root = self._node_union.get(node)
        # 没有该节点，则插入该节点，并且和自身连接
        if root is None:
            self._node_union[node] = node
            self._tree_size[node] = 1
            self.union_count += 1
            return node
        # 找到根,大部分情况下不会进入循环，或循环的次数很少
        while self._node_union[root] != root:
            root = self._node_union[root]
        # 把节点直接连接到根上，削减树的平均深度,大部分情况下不会进入循环，或循环的次数很少
        while self._node_union[node] != root:
            fathernode = self._node_union[node]
            self._node_union[node] = root
            node = fathernode
        return root

    def union(self, node1, node2):
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)
        if root1 == root2:
            return 0
        # 把较小的树连接到较大的树上，使树的平均深度最低
        if self._tree_size[root1] < self._tree_size[root2]:
            self._node_union[root1] = root2
            self._tree_size[root2] += self._tree_size[root1]
            del self._tree_size[root1]
        else:
            self._node_union[root2] = root1
            self._tree_size[root1] += self._tree_size[root2]
            del self._tree_size[root2]
        self.union_count -= 1
        return 1

    def connected(self, node1, node2):
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)
        return root1 == root2


# ================== test ===============
if __name__ == '__main__':
    uf = UnionFind()

    with open('./1_data.txt') as f:
        f.readline()
        for l in f.readlines():
            datas = l.split(' ')
            uf.union(int(datas[0]), int(datas[1]))

    print(uf.union_count)
    print(uf.connected(25, 10))

    uf.union(25, 10)
    print(uf.union_count)
    print(uf.connected(25, 10))
