# coding=utf-8

"""
找到数组中第k大的元素
"""


def select(arr, x):
    """
    找到arr数组中第x大的元素， 该算法同样适用于找到前/后x 大的所有元素。该算法思想源于快排的切分，算法会改变源数组的顺序
    时间复杂度 O(n) , 空间复杂度 O(1)
    :param arr: 源数组
    :param x: 第x大的元素
    :return:
    """
    assert x <= len(arr) and x > 0
    left = 0
    right = len(arr) - 1
    while left < right:
        j = __partition(arr, left, right)
        if j + 1 < x:
            left = j + 1
        elif j + 1 > x:
            right = j - 1
        else:
            # j左边都是小于等于arr[j]的元素， 右边都是大于等于arr[j]的元素
            return arr[j]
    return arr[x - 1]


def __partition(arr, left, right):
    sdindex = __get_mid(arr, left, right)
    __swap(arr, left, sdindex)
    sdvalue = arr[left]
    i = left + 1
    j = right
    while True:
        while arr[i] <= sdvalue and i < right:
            i += 1
        while arr[j] >= sdvalue and j > left:
            j -= 1
        if i >= j:
            break
        __swap(arr, i, j)
    __swap(arr, left, j)
    return j


def __get_mid(arr, left, right):
    mid = int((left + right) / 2)
    if arr[left] < arr[right]:
        if arr[right] <= arr[mid]:
            return right
        elif arr[left] >= arr[mid]:
            return left
        else:
            return mid
    else:
        if arr[left] <= arr[mid]:
            return left
        elif arr[right] >= arr[mid]:
            return right
        else:
            return mid


def __swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


from util import make_random_array

arr = make_random_array(20, 0, 100)
print(arr)
print(select(arr, 3))
print(arr)
