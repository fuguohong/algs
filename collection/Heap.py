# coding=utf-8


def default_compare(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0


class Heap:

    def __init__(self, compare=default_compare):
        """
        堆，最大的值终是在最前面。insert 和 pop 时间复杂度为 logn
        :param compare: (a,b): return (number)
        example :
        构建一个小顶堆。
        def compare(a, b):
            if a < b:
                return 1
            elif a > b:
                return -1
            else:
                return 0
        """
        self._compare = compare
        self._data = [None]
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def values(self):
        return self._data

    def insert(self, data):
        self._size += 1
        if self._size == len(self._data):
            self._data.append(data)
        else:
            self._data[self._size] = data
        self._swim()

    def pop(self):
        if self.is_empty():
            raise Exception('can not pop empty heap')
        data = self._data[1]
        self._swap(1, self._size)
        self._size -= 1
        if len(self._data) > self._size * 2:
            del self._data[self._size + 1:]
        # del self._datas[self._size]
        self._sink()
        return data

    def get_top(self):
        return self._data[1]

    def _swim(self, index=None):
        index = index or self._size
        father = int(index / 2)
        while index > 1 and self._compare(self._data[index], self._data[father]) > 0:
            self._swap(index, father)
            index = father
            father = int(index / 2)
        return index

    def _sink(self, index=1):
        child = index * 2
        while child <= self._size:
            # 存在右节点并且右节点比左节点大， 上浮右节点
            if child + 1 <= self._size and self._compare(self._data[child], self._data[child + 1]) < 0:
                child += 1
            if self._compare(self._data[child], self._data[index]) <= 0:
                break
            self._swap(index, child)
            index = child
            child = index * 2
        return index

    def _swap(self, i, j):
        temp = self._data[i]
        self._data[i] = self._data[j]
        self._data[j] = temp


Heap.default_compare = default_compare

# ================== test ===============
if __name__ == '__main__':
    from util import make_random_array
    import sort


    def rcompare(a, b):
        if a < b:
            return 1
        elif a > b:
            return -1
        else:
            return 0


    heap = Heap()
    arr = make_random_array(20, -100, 100)
    for i in arr:
        heap.insert(i)

    res = []
    while not heap.is_empty():
        res.append(heap.pop())

    print(res)
    print(sort.is_sorted(res))
