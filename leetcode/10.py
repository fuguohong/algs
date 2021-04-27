# coding=utf-8


"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
"""


def merge(nums1, m, nums2, n):
    if n < 1:
        return
    if m < 1:
        nums1[0:n] = nums2[0:n]
    lg = m + n - 1
    i1 = m - 1
    i2 = n - 1
    while lg >= 0:
        if (nums1[i1] > nums2[i2] and i1 >= 0) or i2 < 0:
            nums1[lg] = nums1[i1]
            i1 -= 1
        else:
            nums1[lg] = nums2[i2]
            i2 -= 1
        lg -= 1
