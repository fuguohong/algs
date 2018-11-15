# coding=utf-8

"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


def moveZeroes(nums):
    i = j = 0
    while i < len(nums):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
        i += 1
    while j < len(nums):
        nums[j] = 0
        j += 1


"""
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。
"""


def removeX(nums, val):
    i = 0
    j = -1
    while i < len(nums):
        if nums[i] != val:
            j += 1
            nums[j] = nums[i]
        i += 1
    return j + 1


"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定数组 nums = [1,1,2], 
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
你不需要考虑数组中超出新长度后面的元素。
"""


def removeRept(nums):
    if len(nums) == 0:
        return 0
    i = 1
    j = 0
    while i < len(nums):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
        i += 1
    return j + 1


"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定 nums = [1,1,1,2,2,3],
函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
你不需要考虑数组中超出新长度后面的元素。
"""


def removeRpt2(nums):
    n = len(nums)
    if n < 2:
        return n
    i = 2
    j = 1
    while i < len(nums):
        if nums[i] != nums[j] or nums[i] != nums[j - 1]:
            j += 1
            nums[j] = nums[i]
        i += 1
    return j + 1


arr = [1, 1, 1]

print(removeRpt2(arr))
print(arr)
