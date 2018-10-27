# coding=utf-8

import sort
import random
import time


def sortfn(arr):
    arr.sort()


functions = ('shell_sort', 'merge_sort', 'quick_sort', 'quick_sort_r', 'heap_sort', 'sortfn',)

sortMap = {
    '_select_sort': sort._select_sort,
    '_bubbling_sort': sort._bubbling_sort,
    'insertion_sort': sort.insertion_sort,
    'shell_sort': sort.shell_sort,
    'merge_sort': sort.merge_sort,
    'sortfn': sortfn,
    'quick_sort': sort.quick_sort,
    'quick_sort_r': sort.quick_sort_r,
    'quick_3way': sort.quick_3way,
    'heap_sort': sort.heap_sort,
}


def make_random_array(length, min=0, max=None):
    return [random.randint(min, max or length) for i in range(length)]


def compareSpeed(arr, fns=functions):
    for fn in fns:
        s = arr[:]
        start = time.time()
        sortMap[fn](s)
        print(fn + ' : ' + str(time.time() - start))
        s.reverse()
        assert sort.is_sorted(s)


def is_same(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True


arr = make_random_array(10000)
compareSpeed(arr)
