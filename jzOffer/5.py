# coding=utf-8

"""
p68
用两个栈模拟队列
"""


class Stack:
    def __init__(self):
        self.datas = []

    def push(self, data):
        return self.datas.append(data)

    def top(self):
        if self.is_empty():
            raise Exception('can not pop empty stack')
        return self.datas.pop()

    def is_empty(self):
        return len(self.datas) == 0


class Queue:
    def __init__(self):
        self._insert_stack = Stack()
        self._pop_stack = Stack()

    def append(self, data):
        if self._insert_stack.is_empty():
            self._switch()
        self._insert_stack.push(data)

    def pop(self):
        if self.is_empty():
            raise Exception('can not pop empty queue')
        if self._pop_stack.is_empty():
            self._switch()
        return self._pop_stack.top()

    def is_empty(self):
        return self._insert_stack.is_empty() and self._pop_stack.is_empty()

    def _switch(self):
        if self._insert_stack.is_empty():
            while not self._pop_stack.is_empty():
                self._insert_stack.push(self._pop_stack.top())
        else:
            while not self._insert_stack.is_empty():
                self._pop_stack.push(self._insert_stack.top())


q = Queue()
# a = [1, 2, 3, 4, 5, 6]
# for i in a:
#     q.append(i)

# while not q.is_empty():
#     print(q.pop())


q.append(1)
q.append(2)
print(q.pop())
q.append(6)
q.append(7)
print(q.pop())
print(q.pop())
print(q.pop())