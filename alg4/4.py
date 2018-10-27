# coding=utf-8

"""
p220
一组排列（或是排名）就是一组N个整数的数组，其中0到N-1的每个数都只出现一次。两个排列之间的Kendall tau距离就是在两组数列中顺序不同的数对的数目。
例如a = { 0, 3, 1, 6, 2, 5, 4 } ，b = { 1, 0, 3, 6, 4, 2, 5 }，Kendall tau就是4，
因为就是求两个排列之间的逆序{ 0，1 }，{ 3，1 }，{ 2，4 }，{ 5，4 }，一共为4对，故Kendall tau距离为4。
"""


def distance(arr1, arr2):
    arrlen = len(arr1)
    assert arrlen == len(arr2)
    # arr1中，value出现的位置
    aindex = [0 for i in range(arrlen)]
    # arr2中的value在arr1中出现的位置
    bindex = aindex[:]
    for i in range(arrlen):
        aindex[arr1[i]] = i
    for i in range(arrlen):
        bindex[i] = aindex[arr2[i]]
    # 计算逆序的数量
    return __count(bindex)


def __count(arr):
    count = 0
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp
            j -= 1
            # count即为交换的次数
            count += 1
    return count


x = [0, 3, 1, 6, 2, 5, 4]
y = [1, 0, 3, 6, 4, 2, 5]
print(distance(x, y))
