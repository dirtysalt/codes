#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def flush(wc, buf, ending=False):
            # 如果是最后一行，或者是只有一行输出，模式是相同的
            if ending or len(buf) == 1:
                s = ''
                for w in buf:
                    s = s + w + ' '
                s = s + ' ' * (maxWidth - len(s))
                s = s[:maxWidth]
                return s

            # 其余的时候让空格尽可能地均匀分布
            space = (maxWidth - wc) // (len(buf) - 1)
            more = (maxWidth - wc) % (len(buf) - 1)

            s = ''
            for w in buf:
                s = s + w + ' ' * space
                if more:
                    s = s + ' '
                    more -= 1
            s = s[:maxWidth]
            return s

        ans = []
        buf = []
        wc = 0
        for w in words:
            if (wc + len(w) + len(buf)) > maxWidth:
                ans.append(flush(wc, buf))
                buf.clear()
                wc = 0
            wc += len(w)
            buf.append(w)
        ans.append(flush(wc, buf, ending=True))
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
