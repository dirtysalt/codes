#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        pos = [[] for _ in range(26)]
        for i in reversed(range(len(s))):
            x = ord(s[i]) - ord('a')
            pos[x].append(i)

        C = ord(letter) - ord('a')
        ans = []

        for _ in range(k):
            # early exit.
            if len(ans) + repetition == k:
                ans.extend([C] * repetition)
                break

            # search the min character
            # we have to make sure we can select repetition.
            # but also enough chars that fill k.
            to_index = len(ans) + len(s) - k
            if repetition > 0:
                # print(pos[C])
                to_index = min(to_index, pos[C][repetition - 1])
            trunc_index = to_index

            # we want to know min char before some index.
            for i in range(26):
                ps = pos[i]
                if ps and ps[-1] <= to_index:
                    trunc_index = ps[-1]
                    ans.append(i)
                    if i == C:
                        repetition -= 1
                    break

            # do truncation before that index.
            for i in range(26):
                ps = pos[i]
                while ps and ps[-1] <= trunc_index:
                    ps.pop()

        ans = ''.join(chr(x + ord('a')) for x in ans)
        return ans


true, false, null = True, False, None
cases = [
    ("leet", 3, 'e', 1, 'eet'),
    ("leetcode", 4, 'e', 2, 'ecde'),
    ("bb", 2, 'b', 2, 'bb'),
    ("mmmxmxymmm", 8, "m", 4, "mmmmxmmm"),
    ("aaababcaaa", 8, 'a', 4, 'aaaabaaa'),
    ("aaabbbcccddd", 3, 'b', 2, 'abb'),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().smallestSubsequence, cases)

if __name__ == '__main__':
    pass
