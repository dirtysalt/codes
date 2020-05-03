#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# 返回结果见
# https://developers.google.com/youtube/v3/docs/search

# 参数传入见
# https://developers.google.com/youtube/v3/docs/search/list

# refers to https://developers.google.com/youtube/v3/code_samples/python#search_by_keyword

import hashlib
import json
import pickle as pickle

import pandas as pd
import redis
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

# https://console.developers.google.com/apis/credentials
# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.

DEVELOPER_KEY = "AIzaSyBglP9GAV_zOD3LGhPoIWTAfsEzgAOJ4yU"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

RedisClient = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)


def get_sign(s):
    if not isinstance(s, str):
        s = pickle.dumps(s)
    else:
        s = s.encode('utf8')
    x = hashlib.sha1(s)
    return x.hexdigest()


def read_cache(key):
    key = 'yt.' + get_sign(key)
    v = RedisClient.get(key)
    return json.loads(v) if v is not None else None


def write_cache(key, value, timeout=None):
    key = 'yt.' + get_sign(key)
    value = json.dumps(value)
    if timeout is None:
        RedisClient.set(key, value)
    else:
        RedisClient.setex(key, timeout, value)


def create_youtube_instance():
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    return youtube


youtube = create_youtube_instance()


def youtube_search(options):
    cache_value = read_cache(options)
    if cache_value is not None:
        return cache_value

    print('----- WORKING ON SEARCH -----')
    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        videoDuration=options.videoDuration,
        # maxResults=options.max_results
        # don't change it, otherwise cache invalidates.
        maxResults=options.numsPerPage,
        pageToken=options.pageToken,
        **{'type': 'video'}
    ).execute()

    # videos = []
    # channels = []
    # playlists = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    # for search_result in search_response.get("items", []):
    # if search_result["id"]["kind"] == "youtube#video":
    #   videos.append("%s (%s)" % (search_result["snippet"]["title"],
    #                              search_result["id"]["videoId"]))
    # elif search_result["id"]["kind"] == "youtube#channel":
    #   channels.append("%s (%s)" % (search_result["snippet"]["title"],
    #                                search_result["id"]["channelId"]))
    # elif search_result["id"]["kind"] == "youtube#playlist":
    #   playlists.append("%s (%s)" % (search_result["snippet"]["title"],
    #                                 search_result["id"]["playlistId"]))



    # print "Videos:\n", "\n".join(videos), "\n"
    # print "Channels:\n", "\n".join(channels), "\n"
    # print "Playlists:\n", "\n".join(playlists), "\n"
    res = {'items': search_response.get('items', []),
           'nextPageToken': search_response.get('nextPageToken', None)}
    write_cache(options, res)
    return res


def youtube_search_all(options):
    options.videoDuration = 'short'
    options.pageToken = ''
    options.numsPerPage = 50

    n = options.max_results
    count = 0
    results = []
    while count < n:
        res = youtube_search(options)
        items = res['items']
        nextPageToken = res['nextPageToken']
        if not len(items) or not nextPageToken:
            break
        # print "Videos: \n", "\n".join(map(lambda x: x['snippet']['title'], items))
        options.pageToken = nextPageToken
        count += len(items)
        for x in items:
            results.append({'videoId': x['id']['videoId'],
                            'title': x['snippet']['title'].encode('utf8'),
                            'description': x['snippet']['description'].encode('utf8')})
    return results


def youtube_videos_tags(ids):
    results = {}
    query_ids = []
    for vid in ids:
        k = 'video.' + vid
        value = read_cache(k)
        if value:
            results[vid] = value['snippet'].get('tags', [])
        else:
            query_ids.append(vid)

    idx = 0
    while idx < len(query_ids):
        print('----- WORKING ON TAGS -----')
        sub_ids = query_ids[idx: idx + 50]
        idx += 50
        response = youtube.videos().list(
            id=','.join(sub_ids),
            part='snippet').execute()
        items = response['items']
        for x in items:
            vid = x['id']
            k = 'video.' + vid
            write_cache(k, x)
            results[vid] = x['snippet'].get('tags', [])

    return results


if __name__ == "__main__":
    argparser.add_argument("--q", help="Search term", default="Google")
    argparser.add_argument('--output-file', help="Output file", default="output.csv")
    argparser.add_argument("--max-results", help="Max results", default=100)
    args = argparser.parse_args()

    try:
        # youtube_search(args)
        results = youtube_search_all(args)
        tags = youtube_videos_tags([x['videoId'] for x in results])
        for r in results:
            r['tags'] = (', '.join(tags[r['videoId']])).encode('utf8')
        df = pd.DataFrame(results, columns=('videoId', 'title', 'description', 'tags'))
        df.to_csv(args.output_file, index=False)
    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
