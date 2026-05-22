#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def Leetcode(self, words: List[str]) -> int:
        INF = 1 << 30

        # HELLO LEETCODE
        #        H   E  L   O   T   D   C
        # count  1   4  3   2   1   1   1
        # bits   1   3   2   2   1  1   1
        # off    10  7  5   3   2  1   0
        # mask  0x1 0x7 0x3 0x3 0x1 0x1 0x1
        RULES = {
            # (off, count, mask)
            'h': (10, 1, 0x1),
            'e': (7, 4, 0x7),
            'l': (5, 3, 0x3),
            'o': (3, 2, 0x3),
            't': (2, 1, 0x1),
            'd': (1, 1, 0x1),
            'c': (0, 1, 0x1),
        }
        FINAL = 0b11001110111

        # 第一步预处理并且填充cache.
        cache = [{} for _ in range(len(words))]
        use_dfs = True

        # 使用记忆化搜索的版本
        if not use_dfs:
            # 列举所有的状态
            def list_states():
                states = []
                for st in range(FINAL + 1):
                    ok = True
                    for c, (off, count, mask) in RULES.items():
                        if (st >> off) & mask > count:
                            ok = False
                            break
                    if not ok: continue
                    states.append(st)
                return states

            # 快速过滤不可行的状态
            def fast_check(st, w):
                for c in w:
                    if c in RULES:
                        off, count, mask = RULES[c]
                        if (st >> off) & mask == 0: continue
                        st = st - (1 << off)
                return st == 0

            states = list_states()
            for i in range(len(words)):
                cc = cache[i]

                import functools
                @functools.cache
                def dfs(stm, w):
                    if stm == 0: return 0
                    if not w: return INF
                    ans = INF

                    for j in range(len(w)):
                        c = w[j]
                        if c not in RULES: continue
                        off, count, mask = RULES[c]
                        if (stm >> off) & mask == 0: continue
                        cost = j * (len(w) - 1 - j)
                        if cost >= ans: continue
                        res = dfs(stm - (1 << off), w[:j] + w[j + 1:])
                        ans = min(ans, res + cost)
                    return ans

                for st in states:
                    if not fast_check(st, words[i]): continue
                    res = dfs(st, words[i])
                    if res != INF:
                        cc[st] = res

        # 使用DFS版本.
        else:
            for i in range(len(words)):
                cc = cache[i]

                def dfs(stm, w, tc):
                    if stm not in cc or tc < cc[stm]:
                        cc[stm] = tc

                    for j in range(len(w)):
                        c = w[j]
                        if c not in RULES: continue
                        off, count, mask = RULES[c]
                        if (stm >> off) & mask == count: continue
                        cost = j * (len(w) - 1 - j)
                        stm2 = stm + (1 << off)
                        w2 = w[:j] + w[j + 1:]
                        dfs(stm2, w2, tc + cost)

                dfs(0, words[i], 0)

        def check_state(a, b):
            for c, (off, count, mask) in RULES.items():
                if (a >> off) & mask > (b >> off) & mask:
                    return False
            return True

        import functools
        @functools.cache
        def find_all(stm, i):
            if stm == 0: return 0
            if i == len(words): return INF
            ans = INF
            for st, cost in cache[i].items():
                if cost >= ans: continue  # 剪枝放在check_state之前
                if check_state(st, stm):
                    r = find_all(stm - st, i + 1)
                    ans = min(ans, r + cost)
            return ans

        ans = find_all(FINAL, 0)
        if ans == INF: ans = -1
        return ans


true, false, null = True, False, None
cases = [
    (["hold", "engineer", "cost", "level"], 5),
    (["axer", "qsuec", "rg", "cod", "lauefxbv", "oexyzjr", "yefttp", "gbnpaccl", "lj", "kineyykk", "esecokfl", "qlf",
      "wuxahozg", "z", "py", "ohqpea", "nwrtt", "ixmvpbsw", "jixygsly", "cqiudy"], 2),
    (["lkhqjztn", "cpoipalb", "hrke", "fveuttt", "conrzlm", "tdrohwgm", "odzetred", "jekj", "lh", "kelzwh"], 7),
    (["whlesuln"], -1),
    (["enflwt", "eutchl", "phlfoqs", "oln", "kvdxjw", "nndmjje", "leobff", "dskveexy"], 0),
    (["enflwt", "eutchl", "phlfoqs", "oln", "kvdxjw", "nndmjje", "leobff", "dskveexy", "enflwt", "eutchl", "phlfoqs",
      "oln", "kvdxjw", "nndmjje", "leobff", "dskveexy", "enflwt", "eutchl", "phlfoqs", "oln", "kvdxjw", "nndmjje",
      "leobff", "dskveexy"], 0),
    (["cqjjhwqt", "ecfnltef", "oukqhmhb", "zabxzolm", "eqlhgleq"], -1),
    (["lopoilor", "heuaeqxu", "nzaztvcs", "cwkjp", "etsfern", "zaetijlv", "bzuppj", "cl", "vvxdidw", "los", "clhprxvl"],
     15)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().Leetcode, cases)

if __name__ == '__main__':
    pass

if __name__ == '__main__':
    pass
