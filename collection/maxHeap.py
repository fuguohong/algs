# coding=utf-8


class MaxHeap:
    """
    大顶堆
    """

    def __init__(self):
        self._datas = [None]
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insert(self, data):
        self._datas.append(data)
        self._size += 1
        self._swim()

    def pop(self):
        if self._size < 1:
            raise Exception('can not pop empty heap')
        data = self._datas[1]
        self._swap(1, self._size)
        del self._datas[self._size]
        self._size -= 1
        self._sink()
        return data

    def _swim(self, index=None):
        index = index or self._size
        father = int(index / 2)
        while index > 1 and self._datas[index] > self._datas[father]:
            self._swap(index, father)
            index = father
            father = int(index / 2)

    def _sink(self, index=1):
        child = index * 2
        while child <= self._size:
            # 存在右节点并且右节点比左节点大， 上浮右节点
            if child + 1 <= self._size and self._datas[child + 1] > self._datas[child]:
                child += 1
            if self._datas[child] <= self._datas[index]:
                break
            self._swap(index, child)
            index = child
            child = index * 2

    def _swap(self, i, j):
        temp = self._datas[i]
        self._datas[i] = self._datas[j]
        self._datas[j] = temp


heap = MaxHeap()
from util import make_random_array
import sort

# [787, 332, 281, 717, 532, 798, 365]
arr = make_random_array(20)
for i in arr:
    heap.insert(i)

res = []
while not heap.is_empty():
    res.append(heap.pop())

print(sort.is_sorted(res))
