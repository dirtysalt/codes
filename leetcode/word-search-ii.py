#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def chr2int(c):
    return ord(c) - ord('a')


class Trie:
    def __init__(self):
        self.match_idx = None
        self.nexts = [None] * 26

    def insert(self, s, idx):
        root = self
        for c in s:
            ci = chr2int(c)
            if root.nexts[ci] is None:
                node = Trie()
                root.nexts[ci] = node
            root = root.nexts[ci]
        root.match_idx = idx


class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        n = len(board)
        if n == 0:
            return []
        m = len(board[0])
        if m == 0:
            return []

        res = set()

        def dfs(i, j, root, visited):
            ci = chr2int(board[i][j])
            if root.nexts[ci] is None:
                return
            node = root.nexts[ci]
            if node.match_idx is not None:
                res.add(node.match_idx)
            visited.add((i, j))
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni = di + i
                nj = dj + j

                if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in visited:
                    dfs(ni, nj, node, visited)
            visited.remove((i, j))

        root = Trie()
        for (idx, word) in enumerate(words):
            root.insert(word, idx)

        visited = set()
        for i in range(n):
            for j in range(m):
                assert (len(visited) == 0)
                dfs(i, j, root, visited)

        res = [words[x] for x in list(res)]
        return res


if __name__ == '__main__':
    s = Solution()
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    print(s.findWords(board, words))
