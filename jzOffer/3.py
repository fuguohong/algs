# coding=utf-8

"""
p55
有两个排序的数组A1,A2，A1有足够的空间容纳A2，把A2复制到A1中并保证A1仍然有序
"""


def contact_sort_arr(arr1, arr2):
    assert len(arr1) > len(arr2)
    # 指向arr1 末尾
    pointer_last = len(arr1) - 1
    # 指向arr1 有效部分末尾
    pointer_1 = len(arr1) - len(arr2) - 1
    # 指向arr2末尾
    pointer_2 = len(arr2) - 1
    while pointer_2 >= 0:
        if pointer_1 < 0 or arr2[pointer_2] >= arr1[pointer_1]:
            arr1[pointer_last] = arr2[pointer_2]
            pointer_2 -= 1
        else:
            arr1[pointer_last] = arr1[pointer_1]
            pointer_1 -= 1
        pointer_last -= 1


arr1 = [2, 4, 6, 8, 0, 0, 0, 0]
arr2 = [1, 3, 5, 7]
contact_sort_arr(arr1, arr2)
print(arr1)
assert arr1[0] == 1 and arr1[-1] == 8

arr3 = [1, 2, 3, 4, 0, 0, 0]
arr4 = [5, 6, 7]
contact_sort_arr(arr3, arr4)
print(arr3)
assert arr3[0] == 1 and arr3[-1] == 7

arr5 = [6, 8, 9, 0, 0, 0, 0]
arr6 = [1, 2, 3, 7]
contact_sort_arr(arr5, arr6)
print(arr5)
assert arr5[0] == 1 and arr5[-1] == 9
