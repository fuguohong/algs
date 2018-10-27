# coding=utf-8

"""
p191
只有两个主键的数组排序
"""


def __exch(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def two_key_sort(arr):
    """
    此算法时间复杂度O(n)， 空间复杂度O(1),思想源于快速排序的三向切分
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return
    lt = 0
    opinter = 1
    gt = len(arr) - 1
    while opinter <= gt:
        if arr[opinter] < arr[lt]:
            # 把小的数移动到前面
            __exch(arr, opinter, lt)
            opinter += 1
            lt += 1
        elif arr[opinter] > arr[lt]:
            # 把大的移动到后面
            __exch(arr, opinter, gt)
            gt -= 1
        else:
            opinter += 1


#############################
import test.sort_test
import time

a = test.sort_test.make_random_array(20000, 0, 1)
x = a[:]
start = time.time()
two_key_sort(a)
print(time.time()-start)
test.sort_test.compareSpeed(a)


