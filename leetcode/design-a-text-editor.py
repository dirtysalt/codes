#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Node:
    def __init__(self, ch):
        self.ch = ch
        self.prev = None
        self.next = None


def make_nodes(text):
    head = Node('')
    now = head

    for c in text:
        n = Node(c)
        n.prev = now
        now.next = n
        now = n
    return head.next, now


class TextEditor:

    def __init__(self):
        self.dummy = Node('')
        self.node = self.dummy

    def addText(self, text: str) -> None:
        nn = self.node.next
        head, tail = make_nodes(text)
        self.node.next = head
        head.prev = self.node
        tail.next = nn
        if nn:
            nn.prev = tail
        self.node = tail

    def deleteText(self, k: int) -> int:
        nn = self.node.next
        node = self.node
        ans = 0
        while k and node is not self.dummy:
            k -= 1
            ans += 1
            node = node.prev
        node.next = nn
        if nn:
            nn.prev = node
        self.node = node
        return ans

    def leftContent(self):
        k = 10
        tmp = []
        nn = self.node
        while k > 0 and nn and nn is not self.dummy:
            tmp.append(nn.ch)
            nn = nn.prev
            k -= 1
        return ''.join(tmp[::-1])

    def cursorLeft(self, k: int) -> str:
        node = self.node
        while k and node and node is not self.dummy:
            node = node.prev
            k -= 1
        self.node = node
        return self.leftContent()

    def cursorRight(self, k: int) -> str:
        node = self.node
        while k and node and node.next is not None:
            k -= 1
            node = node.next
        self.node = node
        return self.leftContent()


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)

true, false, null = True, False, None
cases = [
    (["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft",
      "cursorRight"],
     [[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]],
     [null, null, 4, null, "etpractice", "leet", 4, "", "practi"]
     ),
]

import aatest_helper

aatest_helper.run_simulation_cases(TextEditor, cases)

if __name__ == '__main__':
    pass
