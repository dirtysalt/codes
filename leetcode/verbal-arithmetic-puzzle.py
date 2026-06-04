#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def isSolvable(self, words: List[str], result: str) -> bool:
#
#         chars = set(result)
#         for w in words:
#             chars.update(w)
#         chars = list(chars)
#         chars_to_idx = {c: i for i, c in enumerate(chars)}
#
#         words = [[chars_to_idx[x] for x in w] for w in words]
#         result = [chars_to_idx[x] for x in result]
#
#
#         def to_int(s, seq):
#             res = 0
#             for c in s:
#                 res = res * 10 + seq[c]
#             return res
#
#         start_ws = [w[0] for w in words]
#         end_ws = [w[-1] for w in words]
#         start_ws.append(result[0])
#
#         def fast_check(seq):
#             res = 0
#             for w in start_ws:
#                 if seq[w] == 0:
#                     return False
#             for w in end_ws:
#                 res += seq[w]
#             if res % 10 != seq[result[-1]]:
#                 return False
#             return True
#
#         def ok(seq):
#             xs = [to_int(w, seq) for w in words]
#             y = to_int(result, seq)
#             return sum(xs) == y
#
#         for seq in itertools.permutations(list(range(10)), len(chars)):
#             if fast_check(seq) and ok(seq):
#                 return True
#         return False

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:

        chars = set(result)
        for w in words:
            chars.update(w)
        chars = list(chars)
        chars.sort()
        chars_to_idx = {c: i for i, c in enumerate(chars)}
        # print(chars_to_idx)

        words = [[chars_to_idx[x] for x in w] for w in words]
        result = [chars_to_idx[x] for x in result]

        lead = {w[0] for w in words}
        lead.add(result[0])

        # 每个字母的可选数字集合
        mat = []
        for i in range(len(chars)):
            if i in lead:
                mat.append(list(range(1, 10)))
            else:
                mat.append(list(range(10)))

        # 优先挑选在开头的数字，这样可以通过范围判定是否可行
        # 挑选顺序是从每个字符串开头选择一个
        head = set()
        orders = []
        for p in range(7):
            for w in words:
                if p < len(w):
                    x = w[p]
                    if x not in head:
                        orders.append(x)
                        head.add(x)
            if p < len(result):
                x = result[p]
                if x not in head:
                    orders.append(x)
                    head.add(x)
        print(head, orders, result, words)

        # print(orders, tail)

        # for x in mat:
        #     print(x)
        assert len(orders) == len(chars)
        mapping = [-1] * 10
        used = [0] * 10

        def qc():
            res = 0
            for w in words:
                if mapping[w[-1]] == -1:
                    return True
                res += mapping[w[-1]]

            if mapping[result[-1]] == -1:
                return True
            exp = mapping[result[-1]]
            return res % 10 == exp

        def to_int(w):
            res = 0
            for c in w:
                res = res * 10 + mapping[c]
            return res

        def to_int_range(w):
            res = 0
            for (idx, c) in enumerate(w):
                if mapping[c] != -1:
                    res = res * 10 + mapping[c]
                else:
                    shift = (len(w) - idx)
                    base = 10 ** shift
                    return (res * base, (res + 1) * base - 1)

                    # note(yan): 下面这个优化还是不太好用，时间反而提升了200-400ms
                    # 这里如果做更加准确的估计可以缩小范围
                    # min_v, max_v = 0, 9
                    # base = 10 ** (shift - 1)
                    # for v in mat[c]:
                    #     if used[v]:
                    #         continue
                    #     min_v = min(min_v, v)
                    #     max_v = max(max_v, v)
                    # a = (res * 10 + min_v) * base
                    # b = (res * 10 + max_v + 1) * base - 1
                    # return (a, b)

            return (res, res)

        def range_check():
            xs = [to_int_range(w) for w in words]
            x0, x1 = sum([x[0] for x in xs]), sum([x[1] for x in xs])
            ys = to_int_range(result)
            y0, y1 = ys
            if y1 < x0 or y0 > x1:
                return False
            return True

        def test(i):
            # if i == len(tail) and not qc():
            #     return False

            if i == len(orders):
                a = sum((to_int(w) for w in words))
                b = to_int(result)
                return a == b

            # 对范围做检查. 现在所有字符的第一位数字都安排好了
            # if i >= (len(words) + 1) and not range_check():
            #     return False

            # note(yan): 不定等待所有数字都安排好就开始快速检查范围 2000ms->516ms.
            if not range_check():
                return False

            # 针对结尾字符做检查
            if not qc():
                return False

            x = orders[i]
            if mapping[x] != -1:
                if test(i + 1):
                    return True

            else:
                for v in mat[x]:
                    if not used[v]:
                        mapping[x] = v
                        used[v] = 1
                        if test(i + 1):
                            return True
                        used[v] = 0
                        mapping[x] = -1
                return False

        ans = test(0)
        return ans


cases = [
    (["S", "M"], "NX", True),
    (["SEND", "MORE"], "MONEY", True),
    (["THIS", "IS", "TOO"], "FUNNY", True),
    (["LEET", "CODE"], "POINT", False)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().isSolvable, cases)
