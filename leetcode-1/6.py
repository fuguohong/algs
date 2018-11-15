# coding=utf-8

"""
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 无重复字符的最长子串是 "abc"，其长度为 3。
"""


def max_substr_len(s):
    charIndex = dict()  # 保存字符最后出现的index+1
    sublen = 0
    start = 0
    for i in range(len(s)):
        ci = charIndex.get(s[i])
        if ci is not None:
            start = max(ci, start)  # 如果重复位置在本次搜索子串之前，会被忽略
        sublen = max(i - start + 1, sublen)  # start被+1， 所以len要加1
        charIndex[s[i]] = i + 1  # 为了和循环结束时 i = len-1保持一致
    return sublen
