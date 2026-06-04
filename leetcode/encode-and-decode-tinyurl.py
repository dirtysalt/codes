#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import hashlib
import random


def base62(val):
    res = []
    while val:
        c = val % 62
        val = val // 62
        if 0 <= c < 10:
            res.append(chr(c + ord('0')))
        elif 10 <= c < 36:
            res.append(chr(c - 10 + ord('a')))
        else:
            res.append(chr(c - 36 + ord('A')))
    return ''.join(res[::-1])


def unbase62(s):
    val = 0
    for x in s:
        v = 0
        c = ord(x)
        if ord('0') <= c <= ord('9'):
            v = c - ord('0')
        elif ord('a') <= c <= ord('z'):
            v = c - ord('a') + 10
        else:
            v = c - ord('A') + 36
        val = val * 62 + v
    return val


class Codec:
    def __init__(self):
        self.cache = {}
        self.max_val = 1 << 31 - 1

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """

        rnd = random.Random(hashlib.md5(longUrl.encode('utf8')).digest())
        while True:
            val = rnd.randint(0, self.max_val)
            if val not in self.cache or self.cache[val] == longUrl:
                break
        s = base62(val)
        shortUrl = 'http://tinyurl.com/{}'.format(s)
        self.cache[val] = longUrl
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        s = shortUrl[len('http://tinyurl.com/'):]
        val = unbase62(s)
        return self.cache[val]


if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    codec = Codec()
    long_url = 'https://leetcode.com/problems/design-tinyurl'
    short_url = codec.encode(long_url)
    print(short_url)
    print(codec.decode(short_url))
