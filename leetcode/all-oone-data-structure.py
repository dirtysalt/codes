#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# 做一个矩阵列表，
# 行矩阵上元组表示出现X次数的单元，通过双向链表串联起来
# 在行矩阵下面，列也是双向链表
# 至于+1,-1的话，也只需要挪动一格即可

COUNT_NODE = 0
ELEM_NODE = 1


class Node:
    def __init__(self, value, count, type=ELEM_NODE):
        self.value = value
        self.count = count
        self.type = type
        self.up = self.down = self.left = self.right = None

    def row_insert_left(self, head):
        if head.left:
            head.left.right = self
        self.left = head.left
        self.right = head
        head.left = self

    def row_insert_right(self, head):
        if head.right:
            head.right.left = self
        self.right = head.right
        self.left = head
        head.right = self

    def remove(self):
        up = self.up
        down = self.down
        assert up is not None
        up.down = down
        if down:
            down.up = up

    def insert(self, head):
        assert head
        self.down = head.down
        if head.down:
            head.down.up = self
        self.up = head
        head.down = self

    def row_recycle(self, count_nodes):
        if self.count == 0:  # 特殊节点，不做回收
            return

        if self.down is None:
            left = self.left
            right = self.right
            if left:
                left.right = right
            if right:
                right.left = left
            count = self.count
            del count_nodes[count]

    def add_count(self, count_nodes):
        count = self.count
        head = count_nodes[count]
        assert head.type == COUNT_NODE

        if (head.left is None) or (head.left.count != (count + 1)):
            x = Node(value=None, count=count + 1, type=COUNT_NODE)
            count_nodes[count + 1] = x
            x.row_insert_left(head)

        self.remove()
        self.insert(head.left)
        head.row_recycle(count_nodes)
        return head.left  # 可能是最大节点

    def dec_count(self, count_nodes):
        count = self.count
        head = count_nodes[count]
        assert head.type == COUNT_NODE

        if (head.right is None) or (head.right.count != (count - 1)):
            x = Node(value=None, count=count - 1, type=COUNT_NODE)
            count_nodes[count - 1] = x
            x.row_insert_right(head)

        self.remove()
        if count > 1:  # 0 的话我们直接销毁，不用再继续保存
            self.insert(head.right)
        head.row_recycle(count_nodes)


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count_nodes = {}
        self.key_nodes = {}
        self.zero_head = Node(value=None, count=0, type=COUNT_NODE)
        self.count_nodes[0] = self.zero_head
        self.max_head = None

    def print_state(self):
        head = self.max_head
        print('===== state =====')
        while head and head is not self.zero_head:
            print('[{}]:'.format(head.count), end='')
            p = head.down
            while p:
                print(' "{}" '.format(p.value))
                p = p.down
            head = head.right
        print('====== end =====')

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.key_nodes:
            node = Node(value=key, count=0, type=ELEM_NODE)
            self.key_nodes[key] = node
            node.insert(self.zero_head)

        node = self.key_nodes[key]
        res = node.add_count(self.count_nodes)
        node.count += 1

        if self.max_head is None or res.count > self.max_head.count:
            self.max_head = res

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.key_nodes:
            return

        node = self.key_nodes[key]
        node.dec_count(self.count_nodes)
        node.count -= 1

        # 只需要检查max_node是不是被回收了
        if self.max_head.down is None:
            self.max_head = self.max_head.right
            if self.max_head is self.zero_head:
                self.max_head = None

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.max_head:
            x = self.max_head.down
            return x.value
        return ""

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.zero_head.left:
            x = self.zero_head.left.down
            return x.value
        return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

obj = AllOne()
obj.print_state()
obj.inc("hello")
obj.inc("world")
obj.inc("world")
print(obj.getMaxKey())
print(obj.getMinKey())
obj.print_state()
obj.dec("world")
obj.dec("world")
print(obj.getMaxKey())
print(obj.getMinKey())
obj.print_state()
obj.dec("hello")
obj.print_state()
print(obj.getMaxKey())
print(obj.getMinKey())
