# coding=utf-8

"""
p39
长度为n的数组中所有数字都在0到n-1的范围内，确定数组中是否存在重复的数字

要求时间复杂度 O(n) 空间复杂度 O(1)
"""


def hasRepet(nums):
    """
    此算法虽然有双重循环，但是执行时间复杂度为O(n)
    此算法会改变原数组
    :param nums:
    :return:
    """
    assert len(nums) > 0
    for i in range(len(nums)):
        while nums[i] != i:
            if (nums[i] == nums[nums[i]]):
                return True
            temp = nums[i]
            nums[i] = nums[temp]
            nums[temp] = temp
    return False


ipt = [0, 0, 2, 1]

print(hasRepet(ipt))
