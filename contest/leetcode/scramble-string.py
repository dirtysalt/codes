#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution(object):
#     def isScramble(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#
#         # def possibles(s):
#         #     if len(s) <= 1: return [s]
#         #     n = len(s)
#         #     res = set()
#         #     for i in range(1, n):
#         #         ls = possibles(s[:i])
#         #         rs = possibles(s[i:])
#         #         res.update([u + v for u in ls for v in rs])
#         #         res.update([v + u for u in ls for v in rs])
#         #     return tuple(res)
#
#         # res = possibles(s1)
#         # return s2 in res
#
#         if s1 == s2: return True
#         n = len(s1)
#         if n <= 1: return False
#
#         # great , rgate. we got 'gr'
#         # align from left and left.
#
#         # eat and ate. we got 'e'
#         # align from left and right
#         for i in range(1, n):
#             x = ''.join(sorted(s1[:i]))
#             y = ''.join(sorted(s2[:i]))
#             if x == y and \
#                     self.isScramble(s1[:i], s2[:i]) and \
#                     self.isScramble(s1[i:], s2[i:]):
#                 return True
#
#             y = ''.join(sorted(s2[-i:]))
#             if x == y and \
#                     self.isScramble(s1[:i], s2[-i:]) and \
#                     self.isScramble(s1[i:], s2[:-i]):
#                 return True
#         return False


class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        cache = {}

        def dfs(i, j, k):
            if k == 1:
                return s1[i] == s2[j]

            key = '{}.{}.{}'.format(i, j, k)
            if key in cache:
                return cache[key]

            if s1[i:i + k] == s2[j:j + k]:
                ok = True
                cache[key] = ok
                return ok

            ok = False
            for k2 in range(1, k):
                r0 = s1[i:i + k2]
                r1 = s2[j:j + k2]
                if sorted(r0) == sorted(r1):
                    ok = dfs(i, j, k2) and dfs(i + k2, j + k2, k - k2)
                    if ok: break
                r1 = s2[j + k - k2:j + k]
                if sorted(r0) == sorted(r1):
                    ok = dfs(i, j + k - k2, k2) and dfs(i + k2, j, k - k2)
                    if ok: break

            # print(s1[i:i + k], s2[j:j + k], ok)
            cache[key] = ok
            return ok

        k = len(s1)
        ans = dfs(0, 0, k)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.isScramble('great', 'rgtae'))
    print(s.isScramble("abcdefghijklmn", "efghijklmncadb"))
