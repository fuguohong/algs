# coding=utf-8

"""
矩阵每一行每一列数据都是有序递增的，在矩阵中查找某个数据是否存在
"""


def matrixInclude(matrix, data):
    """
    p44
    从右上角到左下角逐步剔除行列，时间复杂度 O(m+n)， m 矩阵行数,n矩阵列数
    如果用二分法剔除行列，则每一次剔除时间复杂度都是log(x)，x=0...m, 0...n
    :param matrix:
    :param data:
    :return:
    """
    assert len(matrix) > 0 and len(matrix[0]) > 0
    axis_x = 0
    axis_y = len(matrix[0]) - 1
    while axis_x < len(matrix) and axis_y >= 0:
        if matrix[axis_x][axis_y] > data:
            axis_y -= 1
        elif matrix[axis_x][axis_y] < data:
            axis_x += 1
        else:
            return True
    return False


ipt = [
    [1, 2, 8, 9],
    [2, 4, 9, 12],
    [5, 7, 10, 13],
    [6, 8, 11, 15],
]

assert matrixInclude(ipt, 9)
assert matrixInclude(ipt, 1)
assert matrixInclude(ipt, 6)
assert matrixInclude(ipt, 15)
assert matrixInclude(ipt, 7)

assert not matrixInclude(ipt, 3)
assert not matrixInclude(ipt, 16)
assert not matrixInclude(ipt, 0)

print('success')
