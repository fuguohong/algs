# coding=utf-8


class Node:
    def __init__(self, key, value=None):
        # 判断key能否比较，python好像没有compareable这种东西，暂时这样实现了
        try:
            key < key
        except Exception:
            raise Exception('key must be comparable')
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BSTree:
    """二叉查找树"""

    def __init__(self):
        self._root = None
        self._size = 0

    def get_size(self):
        return self._size

    def get(self, key):
        node = self._find_node(key)
        if node:
            return node.value
        return None

    def includes(self, key):
        node = self._find_node(key)
        return node is not None

    def set(self, key, value=None):
        self._size += 1
        if self._size == 1:
            self._root = Node(key, value)
            return
        node = self._root
        while True:
            if node.key < key:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(key, value)
                    return 1
            elif node.key > key:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(key, value)
                    return 1
            else:
                node.value = value
                return 0

    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        if node is None:
            return None
        if node.key < key:
            node.right = self._remove(node.right, key)
        elif node.key > key:
            node.left = self._remove(node.left, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            minnode = self._min_node(node.right)
            # 此处left和right顺序不能写反
            minnode.right = self._delmin(node.right)
            minnode.left = node.left
            del node
            return minnode
        return node

    def _delmin(self, node):
        if node is None:
            return None
        if node.left is None:
            return node.right
        node.left = self._delmin(node.left)
        return node

    def _min_node(self, node):
        if node is None:
            return None
        while node.left:
            node = node.left
        return node

    def _find_node(self, key):
        node = self._root
        while node:
            if node.key < key:
                node = node.right
            elif node.key > key:
                node = node.left
            else:
                return node
        return None

    def keys(self):
        arr = self.entires()
        return [k for k, v, in arr]

    def values(self):
        arr = self.entires()
        return [v for k, v, in arr]

    def entires(self):
        arr = []
        self._iotra(arr, self._root)
        return arr

    def _iotra(self, arr, node: Node):
        if node is None:
            return
        self._iotra(arr, node.left)
        arr.append((node.key, node.value))
        self._iotra(arr, node.right)


# ==================== test ==================
if __name__ == "__main__":
    from util import make_random_array

    t = BSTree()
    a = [12, 33, 24, 50, 4, 11, 3, 17, 44, 8, 45]
    print(a)
    for i in a:
        t.set(i)

    t.remove(44)

    for i in t.keys():
        print(i)
