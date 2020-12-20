#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def chr2int(c):
    return ord(c) - ord('a')


class Trie:
    def __init__(self):
        self.match = False
        self.nexts = [None] * 26

    def _op(self, s, op):
        root = self
        for c in s:
            ci = chr2int(c)
            if root.nexts[ci] is None:
                if op == 'insert':
                    node = Trie()
                    root.nexts[ci] = node
                else:
                    return False
            root = root.nexts[ci]
        if op == 'insert':
            root.match = True
        elif op == 'search':
            return root.match
        elif op == 'starts':
            return True

    def insert(self, s):
        self._op(s, 'insert')

    def search(self, s):
        return self._op(s, 'search')

    def startsWith(self, prefix):
        return self._op(prefix, 'starts')

    def dfs_search(self, root, idx, s):
        if idx == len(s):
            return root.match

        for i in range(idx, len(s)):
            c = s[i]
            if c == '.':
                ok = False
                for j in range(26):
                    if root.nexts[j]:
                        ok |= self.dfs_search(root.nexts[j], i + 1, s)
                        if ok: return True
                return False
            ci = chr2int(c)
            if not root.nexts[ci]:
                return False
            root = root.nexts[ci]
        return root.match

    def wild_search(self, s):
        root = self
        return self.dfs_search(root, 0, s)


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.t.insert(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.t.wild_search(word)


if __name__ == '__main__':
    s = WordDictionary()
    s.addWord('bad')
    s.addWord('dad')
    s.addWord('mad')
    print(s.search('sad'))
    print(s.search('bad'))
    print(s.search('.ad'))
    print(s.search('b..'))
