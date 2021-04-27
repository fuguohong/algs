# coding=utf-8

"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的原地算法。
"""


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    arrlen = len(nums)
    shift = k % arrlen
    if shift == 0:
        return
    # index = 0
    # last = nums[0]
    # while True:
    #     next_index = (index + shift) % arrlen
    #     last = nums[next_index] ^ last
    #     nums[next_index] = last ^ nums[next_index]
    #     last = last ^ nums[next_index]
    #     index = next_index
    #     if index == 0:
    #         break
    index = start = 0
    last = nums[index]
    for i in range(arrlen):
        next_index = (index + shift) % arrlen
        last = nums[next_index] ^ last
        nums[next_index] = last ^ nums[next_index]
        last = last ^ nums[next_index]
        index = next_index
        if index == start:
            index = start = start + 1
            last = nums[index]


def rotate2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: python投机法
    """
    shift = k % len(nums)
    nums[:] = nums[-shift:] + nums[:-shift]


input = [1, 2, 3, 4, 5, 6]

rotate2(input, 2)
print(input)
