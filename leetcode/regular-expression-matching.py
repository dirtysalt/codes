#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    # def isMatch(self, s, p):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: bool
    #     """
    #     import re
    #     m = re.match(r'^%s$' % p, s)
    #     if m: return True
    #     else: return False

    def isMatch(self, s, p):
        # to match 'a*' or '.*' against empty string
        s = '#' + s
        # add prefix to avoid index error.
        p = '^' + p
        st = []
        for i in range(len(s)):
            st.append([0] * len(p))
        self.st = st
        st[0][0] = 1

        for i in range(0, len(s)):
            for j in range(1, len(p)):
                if p[j] != '*' and (j + 1) < len(p) and p[j + 1] == '*':
                    continue

                def f():
                    if p[j] == '*':
                        if st[i][j - 2]:
                            return 1

                        match = 0
                        for x in range(i, 0, -1):
                            if p[j - 1] == s[x] or p[j - 1] == '.':
                                if st[x - 1][j - 2]:
                                    match = 1
                                    break
                            else:
                                # 如果字符上不匹配的话就可以断开.
                                break
                        return match
                    if i == 0: return 0
                    return int((p[j] == s[i] or p[j] == '.') and st[i - 1][j - 1])

                match = f()
                st[i][j] = match

        return bool(st[len(s) - 1][len(p) - 1])


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("ab", ".*"))
    print(s.st)
    print('---')
    print(s.isMatch("aab", "c*a*b"))
    print(s.st)
    print('---')
    print(s.isMatch("aaa", "a.a"))
    print(s.st)
    print('---')
    print(s.isMatch("", "."))
    print(s.st)
