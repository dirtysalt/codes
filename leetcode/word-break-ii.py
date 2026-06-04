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

        class Node(object):
            def __init__(self, ch):
                self.ch = ch
                self.word_idx = -1
                self.next = {}

        wordDict = list(wordDict)

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
                    ms.append(head.word_idx)
            return ms

        n = len(s)
        index = buildIndex(wordDict)
        print('build index OK')

        st = []
        for i in range(n + 1):
            st.append(False)
        st[0] = True

        for i in range(n):
            if not st[i]: continue
            ms = tryMatch(s, i, index)
            for m in ms:
                st[i + len(wordDict[m])] = True
        if not st[n]: return []

        st = []
        for i in range(n + 1):
            st.append([])
        st[0].append([])

        for i in range(n):
            rs = st[i]
            if not rs: continue
            ms = tryMatch(s, i, index)
            for m in ms:
                st[i + len(wordDict[m])].extend([x + [m] for x in rs])

        return [' '.join([wordDict[y] for y in x]) for x in st[n]]


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak('leetcode', ['leet', 'code']))
    print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    print(s.wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
    print(s.wordBreak("aaaaaaaa", ["aaaa", "aa", "a"]))
