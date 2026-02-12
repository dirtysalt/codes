#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        def parse_repeat(s, idx):
            val = 0
            while s[idx] != '[':
                val = val * 10 + (ord(s[idx]) - ord('0'))
                idx += 1
            idx, res = parse_string(s, idx + 1)
            assert s[idx] == ']'
            return idx + 1, res * val

        def parse_string(s, idx):
            n = len(s)
            out = []
            while idx < n:
                c = s[idx]
                if c in '0123456789':
                    idx, res = parse_repeat(s, idx)
                    out.append(res)
                elif c == ']':
                    break
                else:
                    out.append(c)
                    idx += 1
            return idx, ''.join(out)

        idx, res = parse_string(s, 0)
        return res


if __name__ == '__main__':
    sol = Solution()
    s = "2[abc]3[cd]ef"
    print(sol.decodeString(s))
    s = "3[a2[c]]"
    print(sol.decodeString(s))
