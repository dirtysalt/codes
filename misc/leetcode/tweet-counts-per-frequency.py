#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class TweetCounts:

    def __init__(self):
        from collections import defaultdict
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            unit = 60
        elif freq == 'hour':
            unit = 3600
        else:
            unit = 3600 * 24

        ans = [0] * ((endTime - startTime) // unit + 1)
        for t in self.tweets[tweetName]:
            if t > endTime or t < startTime:
                continue

            no = (t - startTime + 1) // unit
            ans[no] += 1
        return ans

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
