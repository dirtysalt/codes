#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# note(yan): 这题目前些时间做过类似的
class Solution:
    def reorganizeString(self, S: str) -> str:
        from collections import Counter
        c = Counter(S)
        kvs = sorted(c.items(), key=lambda x: x[1], reverse=True)
        tmp = []
        for k, v in kvs:
            tmp.extend([k] * v)

        n = len(tmp)
        # print(tmp, n)
        ans = [0] * n
        k = 0
        for i in range((n + 1) // 2):
            ans[k] = tmp[i]
            k += 2
        k = 1
        for i in range((n + 1) // 2, n):
            ans[k] = tmp[i]
            k += 2

        for i in range(1, n):
            if ans[i] == ans[i - 1]:
                return ''
        return ''.join(ans)


cases = [
    ('aab', 'aba'),
    ('aabb', 'abab')
]

import aatest_helper

aatest_helper.run_test_cases(Solution().reorganizeString, cases)
