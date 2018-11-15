# coding=utf-8

"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
你可以假设 nums1 和 nums2 不同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
中位数是 (2 + 3)/2 = 2.5
"""


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    mid_index = (len(nums1) + len(nums2)) / 2
    last = [0, 0]
    index = 0
    offset1 = 0
    offset2 = 0
    while index <= mid_index:
        if offset1 >= len(nums1):
            current_num = nums2[offset2]
            offset2 += 1
        elif offset2 >= len(nums2):
            current_num = nums1[offset1]
            offset1 += 1
        elif nums1[offset1] < nums2[offset2]:
            current_num = nums1[offset1]
            offset1 += 1
        else:
            current_num = nums2[offset2]
            offset2 += 1
        last[0] = last[1]
        last[1] = current_num
        index += 1
    if int(mid_index) == mid_index:
        return (last[1] + last[0]) / 2
    else:
        return last[1]


# ================= test ===============
if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))
