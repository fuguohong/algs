# coding=utf-8

"""
实现了各种排序算法
"""


def _select_sort(arr, desc=False):
    """
    选择排序，每次选择最小的元素和当前元素交换位置，效率和输入无关。空间复杂度O(1),时间复杂度O(n^2).不稳定
    :param arr: {list}
    :param desc: {bool} 降序？
    :return: arr
    """
    for i in range(len(arr) - 1):
        min_elm = arr[i]
        for j in range(i + 1, len(arr)):
            if desc ^ (arr[j] < min_elm):
                arr[i] = arr[j]
                arr[j] = min_elm
                min_elm = arr[i]


def _bubbling_sort(arr):
    """
    改进后的冒泡排序，空间复杂度O(1),时间复杂度O(n^2)，最优情况(有序)复杂度(n).稳定
    """
    last_change_index = len(arr) - 1
    has_change = True
    while last_change_index > 0 and has_change:
        has_change = False
        for i in range(last_change_index):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                last_change_index = i
                has_change = True


def insertion_sort(arr):
    """
    插入排序，空间复杂度O(1),时间复杂度O(n^2)，最优情况O(n)，是处理接近有序数组最快的算法。稳定
    """
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            j = i - 1
            while j >= 0 and arr[j] > arr[i]:
                j -= 1
            temp = arr[i]
            arr[j + 2:i + 1] = arr[j + 1:i]
            arr[j + 1] = temp
            # 此为常规语言写法
            # j = i
            # while j > 0 and arr[j] < arr[j-1]:
            #     __exch(arr, j, j-1)
            #     j -= 1


def shell_sort(arr):
    """
    希尔排序（增量排序），空间复杂度O(1)，时间复杂度不确定，性能接近快排。不稳定
    :param arr:
    :return:
    """
    # 确定增量，此处使用的是alg4中使用的增量，len/2 也是一个常用的增量
    gap = 1
    while gap < int(len(arr) / 3):
        gap = gap * 3 + 1
    while gap >= 1:
        for i in range(gap, len(arr)):
            j = i
            nextj = j - gap
            while j >= gap and arr[j] < arr[nextj]:
                __exch(arr, j, nextj)
                j = nextj
                nextj = j - gap
        gap = int(gap / 3)


def merge_sort(arr):
    """
    归并排序，空间复杂度O(n)， 时间复杂度 O(nlogn)，稳定
    :param arr:
    :return:
    """
    cut_size = 10
    __merge_min(arr, cut_size)
    dist = arr[:]
    arrlen = len(arr)
    size = cut_size
    while size < arrlen:
        left = 0
        while left < arrlen - size:
            right = left + size + size - 1
            __merge(arr, dist, left, left + size, min(right, arrlen - 1))
            left = right + 1
        size *= 2


def __merge_min(arr, size):
    arrlen = len(arr)
    if arrlen <= size:
        return insertion_sort(arr)
    for left in range(0, arrlen, size):
        right = min(left + size, len(arr))
        temp = arr[left:right]
        insertion_sort(temp)
        arr[left:right] = temp
        left = right


def __merge(scr, dist, left, sp, right):
    # 把数据从数据复制到辅助空间中
    dist[left: right + 1] = scr[left: right + 1]
    j = left
    k = sp
    for i in range(left, right + 1):
        if j >= sp:
            scr[i] = dist[k]
            k += 1
        elif k > right:
            scr[i] = dist[j]
            j += 1
        elif dist[j] < dist[k]:
            scr[i] = dist[j]
            j += 1
        else:
            scr[i] = dist[k]
            k += 1
        i += 1


def quick_sort(arr):
    """快速排序，非递归版"""
    if len(arr) < 2:
        return
    confine_stack = [0, len(arr) - 1]
    while len(confine_stack) > 0:
        right = confine_stack.pop()
        left = confine_stack.pop()
        spindex = __partition(arr, left, right)
        if spindex - 1 > left:
            confine_stack.append(left)
            confine_stack.append(spindex - 1)
        if spindex + 1 < right:
            confine_stack.append(spindex + 1)
            confine_stack.append(right)


def quick_sort_r(arr):
    """快速排序，递归版"""
    if len(arr) < 2:
        return
    __quick_sort_r(arr, 0, len(arr) - 1)


def __quick_sort_r(arr, left, right):
    if left >= right:
        return
    spindex = __partition(arr, left, right)
    __quick_sort_r(arr, left, spindex - 1)
    __quick_sort_r(arr, spindex + 1, right)


def __partition(arr, left, right):
    """快排切分"""
    sdindex = __get_mid(arr, left, right)
    __exch(arr, left, sdindex)
    sdvalue = arr[left]
    i = left + 1  # 左指针
    j = right  # 右指针
    while True:
        # 从左王右找到区间内大于基准数的位置
        while arr[i] <= sdvalue and i < right:
            i += 1
        # 从右往左找到区间内小与基准数的位置
        while arr[j] >= sdvalue and j > left:
            j -= 1
        # 将大小值交换，使左边总是小于基准数， 右边总是大于基准数
        if j <= i:
            break
        __exch(arr, i, j)
    # 此时j的位置为区间内从左往左最后一个小于基准数的位置， 把基准数放到这里
    __exch(arr, left, j)
    # 返回基准数所在的位置
    return j


def __get_mid(arr, left, right):
    """三样取中"""
    mid = int((left + right) / 2)
    if arr[left] < arr[right]:
        if arr[mid] < arr[left]:
            return left
        elif arr[mid] > arr[right]:
            return right
        else:
            return mid
    else:
        if arr[mid] < arr[right]:
            return right
        elif arr[mid] > arr[left]:
            return left
        else:
            return mid


def quick_3way(arr):
    """三向切分快速排序，适用于包含大量重复键的集合"""
    if len(arr) < 2:
        return
    __quick_3way(arr, 0, len(arr) - 1)


def __quick_3way(arr, left, right):
    if left >= right:
        return
    sdindex = __get_mid(arr, left, right)
    __exch(arr, left, sdindex)
    # 基准值
    sdvalue = arr[left]
    # 移动的指针
    i = left + 1
    # 比基准值小的边界指针
    lt = left
    # 比基准值大的边间指针
    gt = right
    while i <= gt:
        if arr[i] < sdvalue:
            # 把小的值放到左边，移动边界指针
            __exch(arr, i, lt)
            lt += 1
            # i指针处变为基准值，继续向前移动
            i += 1
        elif arr[i] > sdvalue:
            # 把大的值放到右边，移动边界指针，此时i指针处变为原gt值，没有进过比计较，不能移动指针
            __exch(arr, i, gt)
            gt -= 1
        else:
            # 相等，继续移动，与基准值相等的数据不移动
            i += 1
    __quick_3way(arr, left, lt - 1)
    __quick_3way(arr, gt + 1, right)


def heap_sort(arr):
    """堆排序"""
    size = len(arr)
    if size < 2:
        return
    # 构建大顶堆
    last_leaf = int(size / 2) - 1
    for i in range(last_leaf, -1, -1):
        __sink(arr, i, size)
    while size > 1:
        size -= 1
        __exch(arr, 0, size)
        __sink(arr, 0, size)


def __sink(arr, index, size):
    child_node = index * 2 + 1
    while child_node < size:
        # 如果存在右节点,并且右节点比左节点大
        if child_node + 1 < size and arr[child_node] < arr[child_node + 1]:
            child_node += 1
        if arr[child_node] <= arr[index]:
            break
        __exch(arr, index, child_node)
        index = child_node
        child_node = index * 2 + 1


def is_sorted(arr):
    if len(arr) < 3:
        return True
    last_compare = 0
    i = 0
    while i < len(arr) - 1:
        compare = arr[i] - arr[i + 1]
        if compare * last_compare < 0:
            return False
        last_compare = compare
        i += 1
    return True


def __exch(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
