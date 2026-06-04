#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def height(r):
    return r.height if r else 0


def left_rotate(root):
    # print('left_rotate!')
    left = root.left
    root.left = left.right
    root.height = max(height(root.left), height(root.right)) + 1

    left.right = root
    left.height = max(height(left.left), height(left.right)) + 1
    return left


def right_rotate(root):
    # print('right_rotate!')
    right = root.right
    root.right = right.left
    root.height = max(height(root.left), height(root.right)) + 1

    right.left = root
    right.height = max(height(right.left), height(right.right)) + 1
    return right


def balance(root):
    lh = height(root.left)
    rh = height(root.right)

    if (lh - rh) >= 2:
        llh = height(root.left.left)
        lrh = height(root.left.right)
        if lrh > llh:
            root.left = right_rotate(root.left)
        root = left_rotate(root)

    elif (rh - lh) >= 2:
        rlh = height(root.right.left)
        rrh = height(root.right.right)
        if rlh > rrh:
            root.right = left_rotate(root.right)
        root = right_rotate(root)

    else:
        root.height = max(lh, rh) + 1

    return root


class Span:
    def __init__(self, x, y, count=1):
        self.x = x
        self.y = y
        self.count = count

    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.count)

    def overlap(self, other):
        return not (other.x >= self.y or other.y <= self.x)

    def merge(self, other):
        # assume overlap.
        out = []
        x0, y0 = self.x, self.y
        x1, y1 = other.x, other.y
        if x0 > x1:
            out.append(Span(x1, x0, other.count))
            if y0 > y1:
                out.append(Span(x0, y1, self.count + other.count))
                out.append(Span(y1, y0, self.count))
            else:
                out.append(Span(x0, y0, self.count + other.count))
                out.append(Span(y0, y1, other.count))
        else:
            out.append(Span(x0, x1, self.count))
            if y0 > y1:
                out.append(Span(x1, y1, self.count + other.count))
                out.append(Span(y1, y0, self.count))
            else:
                out.append(Span(x1, y0, self.count + other.count))
                out.append(Span(y0, y1, other.count))
        out = [x for x in out if x.x != x.y]
        center, left, right = None, [], []
        for sp in out:
            if sp.x == self.x:
                center = sp
            elif sp.x < self.x:
                left.append(sp)
            else:
                right.append(sp)
        return center, left, right


class Node:
    def __init__(self, span):
        self.span = span
        self.left = None
        self.right = None
        self.height = 1


K = 3


def query(root, span):
    if root is None:
        return True
    rsp = root.span
    if rsp.overlap(span):
        c, l, r = rsp.merge(span)
        if c.count >= K:
            return False
        for x in l:
            if x.count >= K or not query(root.left, x):
                return False
        for x in r:
            if x.count >= K or not query(root.right, x):
                return False
        return True
    elif span.x < rsp.x:
        return query(root.left, span)
    else:
        return query(root.right, span)


def insert(root, span):
    if root is None:
        return Node(span)
    rsp = root.span
    if rsp.overlap(span):
        c, l, r = rsp.merge(span)
        rsp.y = c.y
        rsp.count = c.count
        for x in l:
            root.left = insert(root.left, x)
        for x in r:
            root.right = insert(root.right, x)
    elif span.x < rsp.x:
        root.left = insert(root.left, span)
    else:
        root.right = insert(root.right, span)
    root = balance(root)
    return root


class MyCalendarTwo:
    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        span = Span(start, end)
        if not query(self.root, span):
            return False
        self.root = insert(self.root, span)
        return True
