#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from gevent import monkey;

monkey.patch_all()
from kafka.consumer import KafkaConsumer


# http://kafka-python.readthedocs.org/en/latest/apidoc/kafka.consumer.html#kafka.consumer.KafkaConsumer
# client_id='kafka.consumer.kafka',
# group_id=None,
# fetch_message_max_bytes=1024*1024,
# fetch_min_bytes=1,
# fetch_wait_max_ms=100,
# refresh_leader_backoff_ms=200,
# metadata_broker_list=None,
# socket_timeout_ms=30*1000,
# auto_offset_reset='largest',
# deserializer_class=lambda msg: msg,
# auto_commit_enable=False,
# auto_commit_interval_ms=60 * 1000,
# auto_commit_interval_messages=None,
# consumer_timeout_ms=-1

# http://kafka.apache.org/documentation.html#consumerconfigs
def create_consumer(topics, brokers, group,
                    max_bytes=1024 * 1024, max_wait_ms=100):
    kafka = KafkaConsumer(*topics, metadata_broker_list=brokers,
                          group_id=group,
                          fetch_message_max_bytes=max_bytes,
                          fetch_wait_max_ms=max_wait_ms)
    return kafka


# 只能用单个进程来工作.
# multiple process conumer似乎有问题不能work
# 当然也可以利用下面组件自己开分partition, 但是代价有点高.
def run_worker(cc, f, args, debug=False):
    def wrap_f():
        # create consumer instance.
        consumer = cc()
        while True:
            ms = consumer.fetch_messages()
            for m in ms:
                if debug:
                    print('# receive msg: topic=%s, partition=%d, offset=%d' % (
                        m.topic, m.partition, m.offset))
                r = f(m.value, args)
                consumer.task_done(m)
                if r == 'commit': consumer.commit()

    wrap_f()
