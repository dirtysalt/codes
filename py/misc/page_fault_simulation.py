#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class PageManager:
    def __init__(self, size, access_bits):
        self.st = []
        for i in range(size):
            # -1表示无效页面，0则表示没有访问过
            self.st.append([-1, 0])
        self.size = size
        self.max_access = (1 << access_bits) - 1
        self.pf = 0
        self.clock = 0

    def access(self, page):
        print('access: {}, st: {}'.format(page, self.st))
        # 检查是否缺页
        found = False
        for x in self.st:
            (pn, v) = x
            if pn == page:
                found = True
                x[1] = min(self.max_access, x[1] + 1)
        if found:
            return False

        # 缺页，找到下一个可以替换的页面
        self.pf += 1
        while True:
            c = self.clock
            self.clock = (self.clock + 1) % self.size
            if self.st[c][1] == 0:
                self.st[c] = [page, 0]
                break
            self.st[c][1] -= 1
        return True

def test():
    pm = PageManager(size = 4, access_bits = 2)
    pages = [0,3,2,0,1,3,4,3,1,0,3,2,1,3,4]
    for p in pages:
        pm.access(p)
    print('# of PF = {}'.format(pm.pf))

test()
