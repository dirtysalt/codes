#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class TrieNode:
    def __init__(self):
        self.count = 0
        self.ss = [None] * 26

    def build(self, s, match=False):
        root = self
        for c in s:
            idx = ord(c) - ord('a')
            if root.ss[idx] is None:
                if match:
                    return False, 0
                root.ss[idx] = TrieNode()

            if not match:
                root.count += 1

            subtree = root.ss[idx]
            root = subtree

        if not match:
            root.count += 1

        return True, root.count


if __name__ == '__main__':
    n = int(input())

    trie = TrieNode()

    for n_itr in range(n):
        opContact = input().split()

        op = opContact[0]

        contact = opContact[1]

        if op == 'add':
            trie.build(contact)

        elif op == 'find':
            ok, count = trie.build(contact, match=True)
            print(count)
