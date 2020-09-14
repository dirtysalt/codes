#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class MyQueue(object):
    def __init__(self):
        self.s0 = []
        self.order = 'push'

    def peek(self):
        self.adjust_order('pop')
        return self.s0[-1]

    def pop(self):
        self.adjust_order('pop')
        self.s0.pop()

    def adjust_order(self, order):
        if self.order == order:
            return
        self.s0.reverse()
        self.order = order

    def put(self, value):
        self.adjust_order('push')
        self.s0.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = list(map(int, input().split()))
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print((queue.peek()))
