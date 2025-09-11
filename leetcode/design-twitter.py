#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import defaultdict, deque


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = defaultdict(list)
        self.users = defaultdict(set)
        self.tweet_count = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        tid = self.tweet_count
        self.tweet_count += 1
        self.tweets[userId].append((tid, tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        followees = self.users[userId]
        pool = self.tweets[userId][-10:]
        for x in followees:
            pool.extend(self.tweets[x][-10:])
        pool.sort(key=lambda x: -x[0])
        tweets = [x[1] for x in pool[:10]]
        return tweets

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId == followerId:
            return
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId == followerId:
            return
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
