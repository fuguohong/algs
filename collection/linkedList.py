# coding=utf-8

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def __del__(self):
        del self.data
        del self.nextNode


class LinkedList:
    def __init__(self, iterable=None):
        self._firtNode = None
        self._lastNode = None
        self._length = 0
        if iterable:
            for i in iterable:
                self.insert(i)

    def insert(self, data, index=None):
        """
        插入数据
        :param data: 要插入的数据，
        :param index {int}: 要插入的位置，如果不输入，则向末尾添加数据
        :return: {None}
        """
        newNode = Node(data)
        if not self._firtNode or index == 0:
            temp = self._firtNode
            self._firtNode = newNode
            newNode.nextNode = temp
            self._length += 1
            if not self._lastNode:
                self._lastNode = newNode
            return

        preNode = None
        if not index or index == self._length:
            preNode = self._lastNode
            self._lastNode = newNode
        else:
            preNode = self._fathernode_by_index(index)
        nextNode = preNode.nextNode
        preNode.nextNode = newNode
        newNode.nextNode = nextNode
        self._length += 1

    def get(self, index):
        """
        根据index获取元素，从0开始
        :param index {int}:
        :return: data
        """
        father = self._fathernode_by_index(index)
        return father.nextNode.data

    def replace(self, data, origData=None, index=None):
        """
        将元素替换为data
        :param data: data
        :param origData:  将originData替换为data
        :param index: 将指定位置替换为data， 指定位置后将忽略originData
        :return:
        """
        father = None
        if index != None:
            father = self._fathernode_by_index(index)
        else:
            father = self._fathernode_by_data(origData)[0]
        if not father:
            return
        node = father.nextNode
        origData = node.data
        node.data = data
        return origData

    def index_of(self, data):
        """
        data在链表中的位置，从0开始，如果没有该元素，则返回-1
        :param data:
        :return: index {int}
        """
        node, index = self._fathernode_by_data(data)
        if node:
            return index + 1
        return -1

    def remove(self, data=None, index=None):
        """
        从链表删除一个元素
        :param data: 如果输入data，则从链表中删除data
        :param index: 如果输入index，则删除对应位置的元素（从0开始），如果同时给定data，data会被忽略
        :return: 被删除的元素
        """
        if self._length == 0:
            return
        if index == 0:
            node = self._firtNode
            self._firtNode = node.nextNode
            elm = node.data
            del node
            self._length -= 1
            return elm
        preNode = None
        elm = None
        if index:
            preNode = self._fathernode_by_index(index)
        else:
            preNode = self._fathernode_by_data(data)[0]
        if preNode:
            delNode = preNode.nextNode
            if not delNode:
                raise IndexError
            preNode.nextNode = delNode.nextNode
            elm = delNode.data
            del delNode
            self._length -= 1
        return elm

    def clean(self):
        """
        删除所有元素
        :return:
        """
        node = self._firtNode
        self._firtNode = None
        self._lastNode = None
        self._length = 0
        while node:
            temp = node.nextNode
            del node
            node = temp

    def _fathernode_by_index(self, index):
        if index < 0:
            index = self._length + index
        if index >= self._length or index < 0:
            raise IndexError
        # if (index == self._length):
        #     return self._lastNode
        i = 0
        node = self
        while i < index:
            node = node.nextNode
            i += 1
        return node

    def _fathernode_by_data(self, data):
        father = self
        node = self._firtNode
        index = 0
        while node:
            if node.data == data:
                return (father, index - 1)
            father = node
            node = node.nextNode
            index += 1
        return (None, -1)

    @property
    def nextNode(self):
        return self._firtNode

    @nextNode.setter
    def nextNode(self, value):
        self._firtNode = value

    def __iter__(self):
        nextNode = self._firtNode
        while nextNode:
            yield nextNode.data
            nextNode = nextNode.nextNode

    def __del__(self):
        return self.clean()

    def __len__(self):
        return self._length
