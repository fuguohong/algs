# coding=utf-8


def findKthLargest(nums, k):
    assert k < len(nums)
    left = 0
    right = len(nums) - 1
    while left < right:
        pt = partition(nums, left, right)
        if pt + 1 < k:
            left = pt + 1
        elif pt + 1 > k:
            right = pt - 1
        else:
            return nums[pt]
    return nums[k - 1]


def partition(nums, left, right):
    sentry = int((left + right) / 2)
    mark = nums[sentry]
    switch(nums, sentry, left)
    l = left + 1
    r = right
    while True:
        while nums[l] >= mark and l < right:
            l += 1
        while nums[r] <= mark and r > left:
            r -= 1
        if l >= r:
            break
        switch(nums, l, r)
    switch(nums, left, r)
    return r


def switch(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


arr = [5, 9, 1, 6, 3, 8, 4, 7, 2]

print(findKthLargest(arr,2))
print(arr)
