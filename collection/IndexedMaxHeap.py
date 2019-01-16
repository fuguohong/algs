# coding=utf-8


class IndexedMaxHeap:
    """
    带索引的大顶堆，支持在logn时间内更新、删除元素
    """

    def __init__(self):
        self._data = [None]
        self._index = dict()
        self._size = 0

    def insert(self, element, weight):
        """
        向堆中加入元素
        :param element:  要加入的元素
        :param weight: number,该元素的权重，权重大的元素将会先弹出
        :return: None
        """
        if self.contains(element):
            raise Exception('element has been in this heap. element: ' + element)
        self._size += 1
        # 判断增加元素需要插入还是直接修改无用位置
        if self._size == len(self._data):
            self._data.append([element, weight])
        else:
            self._data[self._size] = [element, weight]
        # 将元素添加到末尾后进行上浮操作
        index = self._swim()
        # 设置元素索引
        self._index[element] = index

    def pop(self):
        """
        弹出权重最大的元素
        :return:
        """
        if self.is_empty():
            raise Exception('can not pop empty heap')
        top = self.get_top()
        self.remove(top)
        return top

    def update(self, element, weight):
        """
        修改element的权重
        :param element:
        :param weight:
        :return:
        """
        eindex = self._index.get(element)
        if eindex is None:
            raise Exception('element dose not in heap. element: ' + element)
        eweight = self._data[eindex][1]
        self._data[eindex][1] = weight
        if eweight < weight:
            self._swim(eindex)
        elif eweight > weight:
            self._sink(eindex)

    def remove(self, element):
        """
        从堆中删除元素
        :param element: 要删除的元素
        :return:
        """
        eindex = self._index.get(element)
        if eindex is None:
            raise Exception('element dose not in heap. element: ' + element)
        eweight = self._data[eindex][1]
        # 将元素和最后一个元素交换位置
        self._swap(eindex, self._size)
        # 删除索引
        del self._index[element]
        # del self._data[self._size]
        # size-1， element所在的末尾位置被废弃
        self._size -= 1
        # 如果空间闲置了一半，删除闲置空间
        if len(self._data) > self._size * 2:
            # 预留1/4使用量的空间
            redundancy = int(self._size / 4) + 1
            del self._data[self._size + redundancy:]
        # 删除的是最后一个元素，就不用上浮或下沉了
        if eindex == self._size + 1:
            return
        # eindex现在是之前的最后一个元素，比较他们的权重
        if eweight < self._data[eindex][1]:
            # 新来的权重大，上浮
            self._swim(eindex)
        elif eweight > self._data[eindex][1]:
            # 新来的权重小，下沉
            self._sink(eindex)

    def get_weight(self, element):
        """
        获取元素的权重
        :param element:
        :return: 权重
        """
        eindex = self._index.get(element)
        if eindex is None:
            raise Exception('element dose not in heap. element: ' + element)
        return self._data[eindex][1]

    def get_elemts(self):
        """
        获取堆中所有元素，不会按权重排序
        :return: 迭代器
        """
        return self._index.keys()

    def get_elemts_with_weight(self):
        """
        获取堆中所有元素及其权重，不会按权重排序
        :return: 迭代器
        """
        return self._index.items()

    def get_top(self):
        """
        获取堆顶元素，不会删除
        :return:
        """
        if self.is_empty():
            return None
        return self._data[1][0]

    def get_size(self):
        """
        获取堆大小
        :return:
        """
        return self._size

    def is_empty(self):
        """
        判断堆是否为空
        :return:
        """
        return self._size == 0

    def contains(self, element):
        """
        判断堆中是否包含某个元素
        :param element:
        :return:
        """
        return element in self._index

    def _swim(self, index=None):
        """
        将位置在index的元素上浮
        :param index:
        :return: 上浮后索引位置
        """
        index = index or self._size
        father = int(index / 2)
        # 没有上浮到顶点，并且权重比父节点大
        while index > 1 and self._data[index][1] > self._data[father][1]:
            # 和父节点交换位置，继续上浮
            self._swap(index, father)
            index = father
            father = int(index / 2)
        return index

    def _sink(self, index=1):
        """
        将位置在index的元素下沉
        :param index:
        :return: 下沉后索引位置
        """
        child = index * 2
        while child <= self._size:
            # 存在右子节点，并且右子节点比左子节点权重大，就和右子节点交换
            if child + 1 <= self._size and self._data[child][1] < self._data[child + 1][1]:
                child += 1
            # 子节点权重大，下沉，交换位置
            if self._data[child][1] > self._data[index][1]:
                self._swap(index, child)
            else:
                # 权重大，下沉
                break
            index = child
            child = index * 2
        return index

    def _swap(self, i, j):
        if i == j:
            return
        temp = self._data[i]
        self._data[i] = self._data[j]
        self._data[j] = temp
        # 交换位置后，修正索引
        self._index[self._data[i][0]] = i
        self._index[self._data[j][0]] = j

    def __contains__(self, item):
        return self.contains(item)


if __name__ == '__main__':
    heap = IndexedMaxHeap()
    # heap.insert('a', 1)
    # heap.insert('b', 2)
    # heap.insert('asd', 4)
    # heap.insert('ad', 9)
    # heap.insert('qq', 2)
    #
    # heap.remove('asd')
    # heap.insert('pp', 12)

    # while not heap.is_empty():
    #     print(heap.pop())

    print(heap.get_top())
