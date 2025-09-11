#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution(object):
#     def findSubstring(self, s, words):
#         """
#         :type s: str
#         :type words: List[str]
#         :rtype: List[int]
#         """
#         nw = len(words[0]) * len(words)
#         if len(s) < nw: return []

#         sign_set = set()
#         import itertools
#         for xs in itertools.permutations(words):
#             sign = 0
#             x = ''.join(xs)
#             for c in x:
#                 sign = sign * 32 + ord(c)
#             print 'x = {}, sign = {}'.format(x, sign)
#             sign_set.add(sign)

#         sign = 0
#         res = []
#         base = 32 ** (nw - 1)
#         for idx in range(0, nw):
#             sign = sign * 32 + ord(s[idx])
#         if sign in sign_set:
#             res.append(0)

#         for idx in range(nw, len(s)):
#             sign -= ord(s[idx - nw]) * base
#             sign = sign * 32 + ord(s[idx])
#             if sign in sign_set:
#                 res.append(idx - nw + 1)

#         return res

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words.sort()
        sws = ''.join(words)
        nw = len(words[0]) * len(words)
        if len(s) < nw: return []

        pf_sign = sum([ord(x) for x in ''.join(words)])
        res = []

        sign = 0
        for idx in range(0, nw):
            sign = sign + ord(s[idx])
        if sign == pf_sign: res.append(0)

        for idx in range(nw, len(s)):
            sign = sign - ord(s[idx - nw]) + ord(s[idx])
            if sign == pf_sign: res.append(idx - nw + 1)

        def post_check(idx):
            xs = []
            for i in range(0, len(words)):
                xs.append(s[idx + i * len(words[0]): idx + (i + 1) * len(words[0])])
            xs.sort()
            ss = ''.join(xs)
            return ss == sws

            # words_dict = {}
            # for w in words:
            #     words_dict[w] = words_dict.get(w, 0) + 1

            # words_set = set(words)
            # for i in range(len(words)):
            #     ss = s[idx + i * len(words[0]) : idx + (i+1)*len(words[0])]
            #     if ss not in words_dict or words_dict[ss] == 0:
            #         return False
            #     words_dict[ss] -= 1
            # return True

        res = [idx for idx in res if post_check(idx)]

        return res


# class Solution(object):
#     def findSubstring(self, s, words):
#         """
#         :type s: str
#         :type words: List[str]
#         :rtype: List[int]
#         """
#         words.sort()
#         sws = ''.join(words)
#         # print sws
#         nw = len(words) * len(words[0])
#         res = []
#         for i in range(0, len(s) - nw + 1):
#             ss = s[i: i + nw]
#             xs = []
#             for j in range(0, len(words)):
#                 xs.append(ss[j*len(words[0]): (j+1)*len(words[0])])
#             xs.sort()
#             # print xs
#             sxs = ''.join(xs)
#             if sxs == sws:
#                 res.append(i)
#         return res

if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo", 'bar']))
    print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
