# coding=utf-8


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


nums1 = [1]
nums2 = []
merge(nums1, 1, nums2, 0)
print(nums1)


# 65-90 97-122 30-39