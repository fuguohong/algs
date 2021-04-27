# coding=utf-8

"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

示例:
输入: numbers = [2, 7, 11, 15], target = 9
输出: [0,1]
"""


def twoSum(self, nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return [left, right]


"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


def twoSum2(nums, target):
    datas = {nums[0]: 0}
    for i in range(1, len(nums)):
        other = target - nums[i]
        if other in datas:
            return [datas[other], i]
        datas[other] = i


a = [2, 7, 11, 15]
print(twoSum2(a, 13))
