# coding=utf-8

"""
红黑树
参考文章：https://www.jianshu.com/p/37c845a5add6
这篇文章的情况不是很全，但是理解其中的内容后缺的情况可以脑补
"""


class Node:
    def __init__(self, key, value=None, is_red=False):
        self.key = key
        self.value = value
        self.is_red = is_red
        self.left = None
        self.right = None


class RBTree:

    def __init__(self):
        self._root = None

    def get(self, key):
        """
        根据key获得相应的值，如果获取不到返回None
        :param key:
        :return: any
        """
        node = self._root
        while node:
            if node.key < key:
                node = node.right
            elif node.key > key:
                node = node.left
            else:
                return node.value
        return None

    def set(self, key, value=None):
        """
        设置值，如果key已经存在，则旧的value被覆盖
        :param key:
        :param value:
        :return:
        """
        self._root = self._set(self._root, key, value)
        self._root.is_red = False

    def remove(self, key):
        """
        根据key删除内容
        :param key:
        :return: value
        """
        if self.is_empty():
            raise Exception("remove from empty tree")
        if not RBTree._is_red(self._root.left):  # 保证当前节点为红色
            self._root.is_red = True
        value = [None]
        self._root = self._remove(self._root, key, value)
        if self.is_empty():
            self._root.is_red = False
        return value[0]

    def is_empty(self):
        return self._root is None

    def keys(self):
        return [k for k, v in self.mo_tra()]

    def values(self):
        return [v for k, v in self.mo_tra()]

    def mo_tra(self):
        """中序遍历"""
        node_stack = []
        entries = []
        node = self._root
        while node or len(node_stack) > 0:
            while node:
                node_stack.append(node)
                node = node.left
            if len(node_stack) > 0:
                n = node_stack.pop()
                entries.append((n.key, n.value))
                node = n.right
        return entries

    def fo_tra(self):
        """前序遍历"""
        node_stack = []
        entries = []
        node = self._root
        while node or len(node_stack) > 0:
            while node:
                node_stack.append(node)
                entries.append((node.key, node.value))
                node = node.left
            if len(node_stack) > 0:
                n = node_stack.pop()
                node = n.right
        return entries

    @staticmethod
    def _delmin(node):
        """
        删除node子节点中key最小的结点
        :param node: 设node必为红色
        :return: {Node} 代替node位置的结点
        """
        # 如果左节点为None， 根据红黑树的黑色平衡性， 其又节点也必然为Node
        if node.left is None:
            return None
        # 继续沿左节点向下
        # 左节点为2-节点， 将其变为红色
        if not RBTree._is_red(node.left) and not RBTree._is_red(node.left.left):
            node = RBTree._left2red(node)
        node.left = RBTree._delmin(node.left)
        return RBTree._balance(node)

    @staticmethod
    def _min_node(node):
        """
        获取node子节点中key最小的结点
        :param node:
        :return: {Node}
        """
        while node.left:
            node = node.left
        return node

    @staticmethod
    def _remove(node, key, value):
        """
        根据key删除结点
        :param node: 当前节点， 必为红色
        :param key:
        :param value:
        :return: {Node} 代替node位置的结点
        """
        # 沿左节点向下
        if key < node.key:
            # 树中没有更小的结点了
            if node.left is None:
                return node
            # 如果将要进入的左结点是2-结点， 保证其为红色
            if not RBTree._is_red(node.left) and not RBTree._is_red(node.left.left):
                node = RBTree._left2red(node)
            node.left = RBTree._remove(node.left, key, value)
        else:
            # 如果左节点是红色，旋转到右节点，方便处理
            if RBTree._is_red(node.left):
                node = RBTree._rotate_right(node)
            # 在树底，直接删除。 （right为null， left不为红色， left必然也为null）
            if node.right is None:
                if node.key == key:
                    value[0] = node.value
                    return None
                else:
                    return node
            # 右节点是2-节点， 将其变为红色
            if not RBTree._is_red(node.right) and not RBTree._is_red(node.right.left):
                node = RBTree._right2red(node)
            if node.key == key:
                value[0] = node.value
                temp = RBTree._min_node(node.right)
                node.key = temp.key
                node.value = temp.value
                node.right = RBTree._delmin(node.right)
            else:
                node.right = RBTree._remove(node.right, key, value)
        return RBTree._balance(node)

    @staticmethod
    def _left2red(node):
        """
        假设左子结点为黑色，将node的左子结点变为红色
        :param node: node总为红色
        :return: {Node} 代替node位置的结点
        """
        RBTree._switch_color(node)
        if RBTree._is_red(node.right.left):  # node的右孩子是红色节点
            # 从右孩子把红色节点借过来
            node.right = RBTree._rotate_right(node.right)
            node = RBTree._rotate_left(node)
            RBTree._switch_color(node)
        return node

    @staticmethod
    def _right2red(node):
        """
        假设右子结点为黑色，node.left为黑色，将node的右子结点变为红色
        :param node: node总为红色
        :return: {Node} 代替node位置的结点
        """
        RBTree._switch_color(node)
        if RBTree._is_red(node.left.left):  # 左节点是3-节点
            # 从左节点借一个节点把右节点变为红色
            node = RBTree._rotate_right(node)
            RBTree._switch_color(node)
        return node

    @staticmethod
    def _balance(node):
        """
        将结点恢复平衡
        :param node:
        :return: {Node} 代替node位置的结点
        """
        if RBTree._is_red(node.right):
            node = RBTree._rotate_left(node)
        if RBTree._is_red(node.left) and RBTree._is_red(node.left.left):
            node = RBTree._rotate_right(node)
        if RBTree._is_red(node.left) and RBTree._is_red(node.right):
            RBTree._switch_color(node)
        return node

    @staticmethod
    def _set(node, key, value):
        if node is None:
            return Node(key, value, True)
        if node.key < key:
            node.right = RBTree._set(node.right, key, value)
        elif node.key > key:
            node.left = RBTree._set(node.left, key, value)
        else:
            node.value = value
            return node
        if RBTree._is_red(node.right) and not RBTree._is_red(node.left):
            node = RBTree._rotate_left(node)
        if RBTree._is_red(node.left) and RBTree._is_red(node.left.left):
            node = RBTree._rotate_right(node)
        if RBTree._is_red(node.right) and RBTree._is_red(node.left):
            RBTree._switch_color(node)
        return node

    @staticmethod
    def _switch_color(node: Node):
        """
        改变颜色。case1: node:red, left:black, right: black.  case2: node:black, left:red, right: red .保证树的黑色平衡
        :param node:
        :return:
        """
        node.is_red = not node.is_red
        node.left.is_red = not node.left.is_red
        node.right.is_red = not node.right.is_red

    @staticmethod
    def _is_red(node: Node):
        if node is None:
            return False
        return node.is_red

    @staticmethod
    def _rotate_right(node: Node):
        """
        右旋转（顺时针）
        :param node:
        :return: {Node} 代替node位置的结点
        """
        newnode = node.left
        newnode.is_red = node.is_red
        node.is_red = True
        node.left = newnode.right
        newnode.right = node
        return newnode

    @staticmethod
    def _rotate_left(node: Node):
        """
        左旋转（逆时针）
        :param node:
        :return: {Node} 代替node位置的结点
        """
        newnode = node.right
        newnode.is_red = node.is_red
        node.is_red = True
        node.right = newnode.left
        newnode.left = node
        return newnode


def is_balance(tree: RBTree):
    """
    测试红黑树是否合法并且平衡
    :param tree:
    :return: bool
    """
    node = tree._root
    result = {"height": 0, "is_balance": True}
    _is_balance(node, False, 0, result)
    return result["is_balance"]


def _is_balance(node, is_red, height, result):
    if node is None:
        if result["height"] == 0:
            result["height"] = height
        else:
            result["is_balance"] = result["height"] == height
        return
    if node.is_red:
        if is_red:
            result["is_balance"] = False
            return
    else:
        height += 1
    _is_balance(node.left, node.is_red, height, result)
    _is_balance(node.right, node.is_red, height, result)


def red_scale(tree):
    """
    统计红黑树中红色节点所占的比例
    :param tree:
    :return: dict
    """
    result = {"red": 0, "nodes": 0}
    _red_scale(tree._root, result)
    result["red_scale"] = result["red"] / result["nodes"]
    return result


def _red_scale(node, result):
    if node is None:
        return
    if node.is_red:
        result["red"] += 1
    result["nodes"] += 1
    _red_scale(node.left, result)
    _red_scale(node.right, result)


# ===================== test =====================
if __name__ == "__main__":
    from util import make_random_array
    from sort import is_sorted

    count = 100
    a = make_random_array(count, 0, count * 10)
    t = RBTree()
    for i in a:
        t.set(i, i)

    assert is_sorted(t.keys())
    assert is_balance(t)

    print('remove: ' + str(t.remove(a[0])))
    print('remove: ' + str(t.remove(a[int(count / 2)])))
    print('remove: ' + str(t.remove(a[count - 1])))
    print('remove: ' + str(t.remove(min(a))))
    print('remove: ' + str(t.remove(max(a))))
    print('remove:' + str(t.remove(count * 20)))

    assert is_balance(t)
    assert is_sorted(t.keys())

    print(t.get(a[20]))
