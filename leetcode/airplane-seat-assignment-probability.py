#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# 这个题目推导公式是这样的：
# 假设N个人的概率是f(N)的话，考虑f(N+1).
# 第一个人如果占据1th位置，那么概率是1.0
# 如果占据2th位置的话，那么2号人可以看做是1号人，此时概率是f(N)
# 。。。 如果占据nth位置的话，概率也是f(N)
# 所以f(N+1) = 1/n + (n-2)/n * f(N)
# 而实际上f(N)=1/2，因为如果带入的话有f(N+1)=1/2.

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1.0
        return 0.5
