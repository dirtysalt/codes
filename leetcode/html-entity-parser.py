#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def entityParser(self, text: str) -> str:
        mapped = {
            '&quot;': '"',
            "&apos;": "'",
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/'
        }
        for f, t in mapped.items():
            text = text.replace(f, t)
        text = text.replace('&amp;', '&')
        return text
