#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Span:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h

    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.h)

    def merge(self, other):
        x0, y0, h0 = self.x, self.y, self.h
        x1, y1, h1 = other.x, other.y, other.h
        out = []

        if y1 < y0:
            if x1 >= x0:
                if h0 >= h1:
                    out.append(Span(x0, y0, h0))
                else:
                    out.append(Span(x0, x1, h0))
                    out.append(Span(x1, y1, h1))
                    out.append(Span(y1, y0, h0))
            else:
                if h0 >= h1:
                    out.append(Span(x1, x0, h1))
                    out.append(Span(x0, y0, h0))
                else:
                    out.append(Span(x1, y1, h1))
                    out.append(Span(y1, y0, h0))

        else:
            if x1 >= x0:
                if h0 >= h1:
                    out.append(Span(x0, y0, h0))
                    out.append(Span(y0, y1, h1))
                else:
                    out.append(Span(x0, x1, h0))
                    out.append(Span(x1, y0, h1))
                    out.append(Span(y0, y1, h1))
            else:
                if h0 >= h1:
                    out.append(Span(x1, x0, h1))
                    out.append(Span(x0, y0, h0))
                    out.append(Span(y0, y1, h1))
                else:
                    out.append(Span(x1, x0, h1))
                    out.append(Span(x0, y0, h1))
                    out.append(Span(y0, y1, h1))

        out = [sp for sp in out if sp.x < sp.y]
        center, left, right = None, [], []
        for sp in out:
            if sp.y == y0:
                center = sp
            elif sp.y > y0:
                right.append(sp)
            else:
                left.append(sp)

        # bad = False
        # for i in range(len(out)):
        #     for j in range(i + 1, len(out)):
        #         if out[i].overlap(out[j]):
        #             print('BAD!!!')
        #             bad = True
        #             break
        #     if bad:
        #         break
        #
        # if bad:
        #     print('++++++++++')
        #     print('{}, {}'.format(self, other))
        #     print('center = {}'.format(center))
        #     print('left = [{}]'.format(', '.join(map(str, left))))
        #     print('right = {}'.format(', '.join(map(str, right))))

        return center, left, right

    def overlap(self, other):
        return not (other.x >= self.y or other.y <= self.x)

    def to_tuple(self):
        return self.x, self.y, self.h


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


def insert_span(root, sp):
    if root is None:
        return Node(sp)
    span = root.value
    if span.overlap(sp):
        center, left, right = span.merge(sp)
        span.x = center.x
        span.h = center.h
        for sp2 in left:
            root.left = insert_span(root.left, sp2)
        for sp2 in right:
            root.right = insert_span(root.right, sp2)
    elif sp.x < span.y:
        assert sp.y <= span.y
        root.left = insert_span(root.left, sp)
    else:
        root.right = insert_span(root.right, sp)
    return root


def list_span(root, res):
    if root is None:
        return
    list_span(root.left, res)
    res.append(root.value)
    list_span(root.right, res)


def merge_span(res):
    if not res:
        return []
    p = res[0]
    out = []
    for i in range(1, len(res)):
        x = res[i]
        if p.y == x.x and p.h == x.h:
            p.y = x.y
        else:
            out.append(p)
            p = x
    out.append(p)
    return out


class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """

    def _buildingOutline(self, buildings):
        # write your code here
        root = None
        for b in buildings:
            span = Span(b[0], b[1], b[2])
            root = insert_span(root, span)
        res = []
        list_span(root, res)
        res = merge_span(res)
        return res

    # lintcode version.
    def buildingOutline(self, buildings):
        buildings.sort(key=lambda x: x[0])
        res = self._buildingOutline(buildings)
        res = [x.to_tuple() for x in res]
        return res

    # leetcode version.
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        res = self._buildingOutline(buildings)
        out = []
        if not res:
            return out
        sp = res[0]
        prev = sp
        out.append([sp.x, sp.h])
        for i in range(1, len(res)):
            sp = res[i]
            if prev.y != sp.x:
                out.append((prev.y, 0))
            out.append([sp.x, sp.h])
            prev = sp
        out.append([prev.y, 0])
        return out
