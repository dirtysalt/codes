#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def longestDecomposition(self, text: str) -> int:
        res = 0
        s, e = 0, len(text) - 1
        while s <= e:
            i, j = s, e
            hs, he = 0, 0

            while True:
                hs += ord(text[i])
                he += ord(text[j])

                if text[s] == text[j]:
                    sz = (e - j + 1)
                    if hs == he and text[s: s + sz] == text[j: j + sz]:
                        # print('matched. {} = {}'.format(
                        #     text[s:s + sz], text[j: j + sz]))
                        res += 1 if (s == j) else 2
                        s = s + sz
                        e = j - 1
                        break

                i += 1
                j -= 1

        return res


import aatest_helper

cases = [
    ('ghiabcdefhelloadamhelloabcdefghi', 7),
    ('antaprezatepzapreanta', 11),
    ('aaa', 3)
]

aatest_helper.run_test_cases(Solution().longestDecomposition, cases)
