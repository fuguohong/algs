# coding=utf-8

"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]

说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。

进阶:
如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""


def sorted_intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    minlen = len(nums1) if len(nums1) < len(nums2) else len(nums2)
    pointer_a = pointer_b = 0
    intersect = []
    while pointer_a < minlen and pointer_b < minlen:
        if nums1[pointer_a] < nums2[pointer_b]:
            pointer_a += 1
        elif nums1[pointer_a] > nums2[pointer_b]:
            pointer_b += 1
        else:
            intersect.append(nums1[pointer_a])
            pointer_a += 1
            pointer_b += 1
    return intersect


ipt1 = [1, 2, 3, 3, 3, 5, 9, 11, 11, 12, 12, 15, 22, 22, 22, 50]
ipt2 = [0, 3, 3, 8, 11, 12, 12, 12, 19, 22, 22, 22, 22, 22, 22, 22]

print(sorted_intersect(ipt1, ipt2))
