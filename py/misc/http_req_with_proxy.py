#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from gevent import monkey
monkey.patch_socket()
import gevent
import urllib.request, urllib.error, urllib.parse

# transparent
# remote_proxy = ('http', '124.206.164.180:3128')
# anonymous
# remote_proxy = ('http', '124.202.182.174:8118')
# remote_proxy = ('http', '52.2.32.237:3128')

remote_proxy = ('http', '127.0.0.1:9000')

# does not work.
# local_proxy = ('socks5', '127.0.0.1:62221')

# req_url = 'http://www.baidu.com'
req_url = 'http://itunes.apple.com/lookup?id=917918570'


def req_with_proxy_0(url, proxy):
    print 'r0 proxy = {} ...'.format(proxy)
    (type, addr) = proxy
    proxy_handler = urllib.request.ProxyHandler({type: addr})
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url)
    data = response.read()
    response.close()
    print 'r0 proxy = {} done'.format(proxy)
    return ('r0', proxy, data)


def req_with_proxy_1(url, proxy):
    print 'r1 proxy = {} ...'.format(proxy)
    (type, addr) = proxy
    req = urllib.request.Request(url)
    req.set_proxy(addr, type)
    f = urllib.request.urlopen(req)
    data = f.read()
    f.close()
    print 'r1 proxy = {} done'.format(proxy)
    return ('r1', proxy, data)

gs = []
gs.append(gevent.spawn(req_with_proxy_0, req_url, remote_proxy))
gs.append(gevent.spawn(req_with_proxy_1, req_url, remote_proxy))
gevent.joinall(gs)
for g in gs:
    (r, proxy, data) = g.value
    print 'r = {}, proxy = {}, size = {}'.format(r, proxy, len(data))
