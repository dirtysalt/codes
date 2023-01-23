#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        for c in s:
            # open paren.
            if c in ('(', '{', '['):
                st.append(c)
                continue
            if not st: return False
            p = st.pop()
            if (c == ')' and p == '(') or \
                    (c == '}' and p == '{') or \
                    (c == ']' and p == '['):
                continue
            return False
        return not st


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('()'))
    print(s.isValid('(([{}]))'))
    print(s.isValid('([)]'))
