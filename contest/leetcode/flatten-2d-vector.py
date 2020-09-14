#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.st = []
        self.st.append((vec2d, 0))

    def _expand(self):
        st = self.st
        while st:
            (obj, idx) = st.pop()
            if isinstance(obj, list):
                if idx == len(obj):
                    continue
                else:
                    st.append((obj, idx + 1))
                    st.append((obj[idx], 0))
            else:
                st.append((obj, idx))
                break

    # @return {int} a next element
    def next(self):
        # Write your code here
        st = self.st
        obj, idx = st.pop()
        return obj

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        self._expand()
        return self.st
