#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import gevent.monkey
import uuid

gevent.monkey.patch_all()
import gevent.pool

import os.path
import requests

# UPLOAD_URL = "http://localhost:9998/upload"
UPLOAD_URL = "http://utils.castbox.fm/file_upload/multiple_uploads_to_s3?file_ext=py"
# UPLOAD_URL = "http://localhost:9998/file_upload/multiple_uploads_to_s3"
SEGMENT_SIZE = 400


# def upload(fp, session_id, file_pos, size, file_size):
#     fp.seek(file_pos)
#     payload = fp.read(size)
#     content_range = "bytes {file_pos}-{pos_end}/{file_size}".format(file_pos=file_pos,
#                                                                     pos_end=file_pos + size - 1, file_size=file_size)
#     headers = {'Content-Disposition': 'attachment; filename="big.TXT"', 'Content-Type': 'application/octet-stream',
#                'X-Content-Range': content_range, 'Session-ID': session_id, 'Content-Length': str(size)}
#     res = requests.post(UPLOAD_URL, data=payload, headers=headers)
#     print(res.text)

def upload(req):
    payload, file_pos, session_id, file_size = req
    size = len(payload)
    content_range = "bytes {file_pos}-{pos_end}/{file_size}".format(file_pos=file_pos,
                                                                    pos_end=file_pos + size - 1, file_size=file_size)
    headers = {'Content-Disposition': 'attachment; filename="filename.data"',
               'Content-Type': 'text/plain',
               'X-Content-Range': content_range, 'Session-ID': session_id, 'Content-Length': str(size)}
    res = requests.post(UPLOAD_URL, data=payload, headers=headers)
    # print('content-range = {}, resp = {}, headers = {}'.format(content_range, res.text, res.headers))
    print('resp = {}'.format(res.text))


def main():
    session_id = uuid.uuid4().hex
    f = __file__
    file_pos = 0
    file_size = os.path.getsize(f)
    fp = open(f, "r")

    reqs = []
    while True:
        fp.seek(file_pos)
        payload = fp.read(SEGMENT_SIZE)
        reqs.append((payload, file_pos, session_id, file_size))
        file_pos += SEGMENT_SIZE

        if file_pos >= file_size:
            fp.close()
            break

    pool = gevent.pool.Pool()
    for req in reqs:
        pool.spawn(upload, req)
    pool.join()
    print('OK')


if __name__ == "__main__":
    main()
