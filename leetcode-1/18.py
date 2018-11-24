# coding=utf-8

'''
 * https://leetcode-cn.com/explore/orignial/card/all-about-lockup-table/239/learn-to-use-keys/1003/
 * 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
 *
 * 输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
  输出: 4
'''

from fractions import Fraction
import sys


def maxPoints(potints):
    l = len(potints)
    if l == 0:
        return 0
    if l < 3:
        return l
    m = 0
    for i in range(l):
        m = max(m, linePoints(potints, potints[i]))
    return m


def linePoints(points, point):
    slopes = dict()
    same = 0
    for i in range(len(points)):
        if point[0] == points[i][0] and point[1] == points[i][1]:
            same += 1
            continue
        divnum = points[i][0] - point[0]
        if divnum == 0:
            slope = sys.float_info.max
        else:
            slope = Fraction(points[i][1] - point[1], divnum)
        c = slopes.get(slope)
        slope[slope] = 1 if c is None else c + 1
    return max(slopes.values()) + same


print(maxPoints([ [ 0, 0 ], [ 94911151, 94911150 ], [ 94911152, 94911151 ] ]))
