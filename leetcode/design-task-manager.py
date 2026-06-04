#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        from sortedcontainers import SortedList
        self.sl = SortedList()
        self.tsk = {}
        for u, t, p in tasks:
            self.add(u, t, p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tsk[taskId] = (userId, priority)
        self.sl.add((priority, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        (u, p) = self.tsk[taskId]
        self.sl.remove((p, taskId))
        self.sl.add((newPriority, taskId))
        self.tsk[taskId] = (u, newPriority)

    def rmv(self, taskId: int) -> None:
        (u, p) = self.tsk[taskId]
        self.sl.remove((p, taskId))
        del self.tsk[taskId]

    def execTop(self) -> int:
        if not self.sl:
            return -1
        (p, t) = self.sl.pop()
        (u, p) = self.tsk[t]
        del self.tsk[t]
        return u


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()

if __name__ == '__main__':
    pass
