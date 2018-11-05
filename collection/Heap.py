# coding=utf-8


def comparefn(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0


class Heap:

    def __init__(self, compare=comparefn):
        """
        堆，最大的值终是在最前面。insert 和 pop 时间复杂度为 lgn
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
        self._datas = [None]
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def values(self):
        return self._datas

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
        while index > 1 and self._compare(self._datas[index], self._datas[father]) > 0:
            self._swap(index, father)
            index = father
            father = int(index / 2)

    def _sink(self, index=1):
        child = index * 2
        while child <= self._size:
            # 存在右节点并且右节点比左节点大， 上浮右节点
            if child + 1 <= self._size and self._compare(self._datas[child], self._datas[child + 1]) < 0:
                child += 1
            if self._compare(self._datas[child], self._datas[index]) <= 0:
                break
            self._swap(index, child)
            index = child
            child = index * 2

    def _swap(self, i, j):
        temp = self._datas[i]
        self._datas[i] = self._datas[j]
        self._datas[j] = temp


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
    arr = [5, 9, 7, 1, 6, 4, 3]
    for i in arr:
        heap.insert(i)

    res = []
    while not heap.is_empty():
        res.append(heap.pop())

    print(res)
    print(sort.is_sorted(res))
