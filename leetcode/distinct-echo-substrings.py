#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


# class Solution:
#     def distinctEchoSubstrings(self, text: str) -> int:
#         n = len(text)
#         from collections import defaultdict
#         bk = defaultdict(list)

#         for i in range(n):
#             for j in range(i, n):
#                 s = text[i:j+1]
#                 bk[s].append(i)
#                 bk[s].append(j+1)

#         res = 0
#         for s, ps in bk.items():
#             ps.sort()
#             for i in range(1, len(ps)):
#                 if ps[i] == ps[i-1]:
#                     res += 1
#                     break

#         return res

# class Solution:
#     def distinctEchoSubstrings(self, text: str) -> int:
#         n = len(text)
#         from collections import defaultdict

#         bk = defaultdict(list)

#         for i in range(n):
#             for j in range(i, n):
#                 s = text[i:j+1]
#                 h = hash(s)
#                 bk[h].append(i)
#                 bk[h].append(j+1)

#         res = 0
#         for s, ps in bk.items():
#             ps.sort()
#             for i in range(1, len(ps)):
#                 if ps[i] == ps[i-1]:
#                     res += 1
#                     break

#         return res

# class Solution:
#     def distinctEchoSubstrings(self, text: str) -> int:
#         n = len(text)
#         res = 0

#         from collections import defaultdict
#         for sz in range(1, n):

#             bk = defaultdict(list)
#             for i in range(0, n - sz + 1):
#                 s = text[i: i + sz]
#                 bk[s].append(i)
#                 bk[s].append(i + sz)

#             for s, ps in bk.items():
#                 ps.sort()
#                 for i in range(1, len(ps)):
#                     if ps[i] == ps[i-1]:
#                         res += 1
#                         break

#         return res

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        res = 0

        # 对长度为1的字符串特殊处理
        bk = [0] * 26
        for i in range(1, n):
            c = ord(text[i]) - ord('a')
            if bk[c]:
                continue
            if text[i] == text[i-1]:
                res += 1
                bk[c] = 1

        # 性能瓶颈在动态计算hash上
        from collections import defaultdict
        for sz in range(2, n // 2 + 1):
            bk = defaultdict(set)
            removed = set()
            for i in range(0, n - sz + 1):
                s = text[i: i + sz]
                if s in removed:
                    continue

                st = bk[s]
                if i in st:
                    res += 1
                    removed.add(s)
                st.add(i + sz)

        return res


import aatest_helper

cases = [
    ("abcabcabc", 3),
    ("leetcodeleetcode", 2),
    ("tkfbgwgqvdsbnukcpxlpifuhbvtdxhhhqurotspohiuwhblnra", 1),
    ("aaaaaaaaaa", 5)
]

aatest_helper.run_test_cases(Solution().distinctEchoSubstrings, cases)
