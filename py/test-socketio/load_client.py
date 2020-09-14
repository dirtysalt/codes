#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import socketio
from gevent import monkey

monkey.patch_all()

import xutil

import argparse
import time
from socket import socket as Socket

import tdigest
from gevent.pool import Pool as ThreadPool
from multiprocessing import Queue as MPQueue, Process

logger = xutil.logger


def get_time_ts():
    return int(time.time() * 1000)


class GlobalState:
    def __init__(self):
        self.current_conn_number = 0
        self.rcv_msg_number = 0
        self.digest = tdigest.TDigest()
        self.conn_digest = tdigest.TDigest()

    def __str__(self):
        digest = self.conn_digest
        msg1 = 'create conn: p50 = {:.2f}, p90 = {:.2f}, p99 = {:.2f}'.format(
            digest.percentile(50), digest.percentile(90), digest.percentile(99))
        digest = self.digest
        msg2 = 'recv message: p50 = {:.2f}, p90 = {:.2f}, p99 = {:.2f}'.format(
            digest.percentile(50), digest.percentile(90), digest.percentile(99))
        return msg1 + ', ' + msg2


class FanoutNamespace(socketio.ClientNamespace):
    def __init__(self, st: GlobalState, io, path):
        # logger.info('__init__, path = {}'.format(path))
        super(FanoutNamespace, self).__init__(io, path)
        self.st = st
        self.init_time = get_time_ts()

    def on_connect(self):
        logger.info('on connect')
        self.st.current_conn_number += 1
        now = get_time_ts()
        delay = (now - self.init_time)
        self.st.conn_digest.update(delay)

    def on_disconnect(self):
        logger.info('on disconnect')
        self.st.current_conn_number -= 1

    def on_message(self, data):
        logger.info('on message. msg = {}'.format(data))

    def on_my_event(self, data):
        logger.info('on my event. msg = {}'.format(data))
        if data == 'quit':
            self.st.rcv_msg_number += 1
            return
        ts = int(data)
        now = get_time_ts()
        delay = (now - ts)
        self.st.digest.update(delay)


parser = argparse.ArgumentParser()
parser.add_argument('--batch-size', action='store', default=10, type=int)
parser.add_argument('--batch-round', action='store', default=10, type=int)
parser.add_argument('--port', action='store', default=8080, type=int)
parser.add_argument('--namespace', action='store', default='/fanout', type=str)
parser.add_argument('--host', action='store', default='127.0.0.1', type=str)
parser.add_argument('--bind', action='store', default='127.0.0.1', type=str)
parser.add_argument('--workers', action='store', default=1, type=int)
args = parser.parse_args()

batch_size = args.batch_size
batch_round = args.batch_round
total_conn_number = batch_round * batch_size
workers = args.workers
port = args.port
host = args.host
binds = args.bind.split(',')


def run(bind_address, _worker_idx):
    worker_name = '(bind = {}, w = {})'.format(bind_address, _worker_idx)
    _socket_connect = Socket.connect

    def my_socket_connect(self: Socket, address):
        # logger.warning('socket {} bind to {}'.format(self, args.bind))
        self.bind((bind_address, 0))
        return _socket_connect(self, address)

    Socket.connect = my_socket_connect

    pool = ThreadPool()
    socks = []

    state = GlobalState()

    class BindFanoutNamespace(FanoutNamespace):
        def __init__(self, io, path):
            super(BindFanoutNamespace, self).__init__(state, io, path)

    for rnd in range(batch_round):
        logger.warning('{}: round #{} start'.format(worker_name, rnd))
        exp_conn_number = (rnd + 1) * batch_size
        for i in range(batch_size):
            sock = socketio.Client()
            sock.register_namespace(BindFanoutNamespace(args.namespace))
            url = 'http://{}:{}'.format(host, port)
            sock.connect(url)
            socks.append(sock)
            pool.spawn(sock.wait)
        while state.current_conn_number != exp_conn_number:
            logger.warning(
                '{}: current_conn = {}, exp_conn = {}'.format(worker_name, state.current_conn_number, exp_conn_number))
            time.sleep(5)
        logger.warning('{}: round #{} ok. current_conn = {}'.format(worker_name, rnd, state.current_conn_number))

    while state.rcv_msg_number != total_conn_number:
        logger.warning('{}: rcv_msg = {}, total_conn = {}'.format(
            worker_name, state.rcv_msg_number, total_conn_number))
        time.sleep(2)

    for rnd in range(batch_round):
        logger.warning('{}: round #{} quit'.format(worker_name, rnd))
        exp_conn_number = (batch_round - rnd - 1) * batch_size
        for s in socks[rnd * batch_size: (rnd + 1) * batch_size]:
            s.disconnect(path=args.namespace)
            s.disconnect()
        while state.current_conn_number != exp_conn_number:
            logger.warning(
                '{}: current_conn = {}, exp_conn = {}'.format(worker_name, state.current_conn_number, exp_conn_number))
            time.sleep(5)
    # for s in socks:
    #     s._close()
    empty = pool.join(timeout=10, raise_error=False)
    if not empty:
        logger.warning('{} join timeout. kill it'.format(worker_name))
        pool.kill()
    logger.warning('{} QUIT !!!'.format(worker_name))
    # return state
    return '{}: {}'.format(worker_name, str(state))


def call(q: MPQueue, func, *args):
    result = func(*args)
    q.put(result)
    q.close()


result_queue = MPQueue()

ps = []
for bind in binds:
    for w in range(workers):
        print('bind = {}, w = {}'.format(bind, w))
        p = Process(target=call, args=(result_queue, run, bind, w))
        p.start()
        ps.append(p)

states = []
while len(states) != len(ps):
    state = result_queue.get()
    states.append(state)

for state in states:
    logger.warning('state = {}'.format(state))
