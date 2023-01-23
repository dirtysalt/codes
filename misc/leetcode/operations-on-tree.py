#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class State:
    def __init__(self, p):
        self.lock = 0
        self.user = 0
        self.child = []
        self.parent = p


class LockingTree:

    def __init__(self, parent: List[int]):
        n = len(parent)
        self.state = [State(parent[i]) for i in range(n)]
        for i in range(n):
            p = parent[i]
            if p != -1:
                self.state[p].child.append(i)

    def unlock_all(self, num):
        from collections import deque
        dq = deque()
        dq.append(num)
        while dq:
            x = dq.popleft()
            st = self.state[x]
            st.user = 0
            st.lock = 0
            for c in self.state[x].child:
                dq.append(c)

    def lock(self, num: int, user: int) -> bool:
        st = self.state[num]
        if st.user == 0:
            st.user = user

            x = num
            while x != -1:
                self.state[x].lock += 1
                x = self.state[x].parent
            return True

        return False

    def unlock(self, num: int, user: int) -> bool:
        st = self.state[num]
        if st.user == user:
            st.user = 0

            x = num
            while x != -1:
                self.state[x].lock -= 1
                x = self.state[x].parent
            return True

        return False

    def upgrade(self, num: int, user: int) -> bool:
        if self.state[num].lock == 0:
            return False

        cut = self.state[num].lock
        x = num
        while x != -1:
            if self.state[x].user != 0:
                return False
            x = self.state[x].parent

        self.unlock_all(num)
        st = self.state[num]
        x = num
        while x != -1:
            self.state[x].lock -= (cut - 1)
            x = self.state[x].parent
        st.user = user
        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)

true, false, null = True, False, None
cases = [
    (["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"],
     [[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]],
     [null, true, false, true, true, true, false]),
]

import aatest_helper

aatest_helper.run_simulation_cases(LockingTree, cases)

if __name__ == '__main__':
    pass
