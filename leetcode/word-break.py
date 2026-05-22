#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        wordDict = list(wordDict)

        class Node(object):
            def __init__(self, ch):
                self.ch = ch
                self.word_idx = -1
                self.next = {}

        def buildIndex(wordDict):
            root = Node('R')
            for (idx, w) in enumerate(wordDict):
                head = root
                for c in w:
                    if c not in head.next:
                        n = Node(c)
                        head.next[c] = n
                    head = head.next[c]
                head.word_idx = idx
            return root

        def tryMatch(s, i, head):
            ms = []
            for j in range(i, len(s)):
                c = s[j]
                if c not in head.next:
                    break
                head = head.next[c]
                if head.word_idx != -1:
                    ms.append(j)
            return ms

        n = len(s)
        index = buildIndex(wordDict)

        st = []
        for i in range(n + 1):
            st.append(False)
        st[0] = True

        for i in range(n):
            if not st[i]: continue
            ms = tryMatch(s, i, index)
            for m in ms:
                st[m + 1] = True
        return st[n]


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak('leetcode', ['leet', 'code']))
    print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
