# coding=utf-8

"""
逆序输出链表
"""

from collections.linkedList import LinkedList


def revers_print(list):
    temp = LinkedList()
    for i in list:
        temp.insert(i, 0)
    for i in temp:
        print(i)


def revers_print2(list):
    if isinstance(list, LinkedList):
        list = list.nextNode
    if list.nextNode:
        revers_print2(list.nextNode)
    print(list.data)


list = LinkedList((1, 2, 3, 4, 5, 6, 7))
revers_print2(list)
