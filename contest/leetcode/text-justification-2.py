#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        ans = []
        sz = 0
        st = []

        def flush_middle(st, sz):
            if len(st) == 1:
                st.append('')

            avg = (maxWidth - sz) // (len(st) - 1)
            more = (maxWidth - sz) % (len(st) - 1)
            res = ''
            for w in st[:-1]:
                res += w
                res += ' ' * (avg + (1 if more > 0 else 0))
                more -= 1
            res += st[-1]
            print('>>>MID', res)
            ans.append(res)
            return res

        def flush_end(st, sz):
            res = ''
            for w in st[:-1]:
                res += w
                res += ' '
            res += st[-1]
            res += ' ' * (maxWidth - sz - len(st) + 1)
            print('>>>END', res)
            ans.append(res)
            return res

        for w in words:
            if sz + len(st) + len(w) > maxWidth:
                flush_middle(st, sz)
                st.clear()
                sz = 0
            st.append(w)
            sz += len(w)

        flush_end(st, sz)
        return ans


cases = [
    (["This", "is", "an", "example", "of", "text", "justification."], 16, [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]),
    (["What", "must", "be", "acknowledgment", "shall", "be"], 16, [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]),
    (["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
      "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20, [
         "Science  is  what we",
         "understand      well",
         "enough to explain to",
         "a  computer.  Art is",
         "everything  else  we",
         "do                  "
     ])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().fullJustify, cases)
