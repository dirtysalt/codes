#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from __future__ import print_function

import cPickle
import itertools
import os
import time
from collections import defaultdict

import numpy as np
import pandas as pd
import scipy
import scipy.sparse
from core import feed_mgr
from core.handler import TCastBoxInstallation, TEverestInstallation, TEverestUser, TPodcast, TUserData
from lightfm import LightFM
from tqdm import tqdm as mytqdm

DATA_DIR = './data/'
USER_ITEM_MAT_PATH = DATA_DIR + 'user_item_mat'
EVST_USER_ITEM_PATH = DATA_DIR + 'evst_user_item_mat'
LOCALE_ITEM_MAT_PATH = DATA_DIR + 'locale_item_mat'

LOCALE_RECOMM_DATA_PATH = DATA_DIR + 'locale_recomm.data'
ITEM_RECOMM_DATA_PATH = DATA_DIR + 'item_recomm.data'

TRAIN_USER_ITEM_MAT_PATH = DATA_DIR + 'train_user_item_mat'
TEST_USER_ITEM_MAT_PATH = DATA_DIR + 'test_user_item_mat'
TRAIN_USER_ITEM_META_PATH = DATA_DIR + 'train_user_item_meta.csv'
TEST_USER_ITEM_META_PATH = DATA_DIR + 'test_user_item_meta.csv'

EVST_TRAIN_USER_ITEM_MAT_PATH = DATA_DIR + 'evst_train_user_item_mat'
EVST_TEST_USER_ITEM_MAT_PATH = DATA_DIR + 'evst_test_user_item_mat'
EVST_TRAIN_USER_ITEM_META_PATH = DATA_DIR + 'evst_train_user_item_meta.csv'
EVST_TEST_USER_ITEM_META_PATH = DATA_DIR + 'evst_test_user_item_meta.csv'

os.environ['OPENBLAS_NUM_THREADS'] = '1'
_g_user_helper = None
_g_channel_helper = None


def get_user_helper():
    global _g_user_helper
    if not _g_user_helper:
        channel_helper = get_channel_helper()
        _g_user_helper = UserHelper(channel_helper)
    return _g_user_helper


def get_channel_helper():
    global _g_channel_helper
    if not _g_channel_helper:
        _g_channel_helper = ChannelHelper()
    return _g_channel_helper


def save_mat(path, mat, compressed=False):
    scipy.sparse.save_npz(path, mat, compressed=compressed)


def load_mat(path):
    return scipy.sparse.load_npz(path + '.npz')


def _export_channel_data():
    query = feed_mgr.make_parsed_query()
    rs = TPodcast.find(query)
    cdata = {}
    for r in rs:
        key = r['key']
        pid = r.get('pid')
        track_key = r.get('track_id')
        if not pid:
            continue
        jump_key = r.get('jump_key')
        title = r.get('title', '')
        lang = r.get('language', '')
        private = 1 if r.get('private') else 0
        data = {
            'pid': pid,
            'title': title,
            'lang': lang,
            'jump': jump_key,
            'track': track_key,
            'key': key,
            'private': private
        }
        cdata[key] = data
    return cdata


class ChannelHelper:
    def __init__(self):
        self.meta_data_path = DATA_DIR + 'channel_meta.data'
        self.index_data_path = DATA_DIR + 'channel_index.data'
        self.channel_data = None
        self.channel_pid_data = None
        self.channel_cid2idx = None
        self.channel_idx2cid = None

    def dump_meta_data(self):
        channel_data = _export_channel_data()
        with open(self.meta_data_path, 'w') as fh:
            cPickle.dump(channel_data, fh)

    def key_to_pid(self, key):
        if key.startswith('pod-'):
            key = key[4:]
        y = self.channel_data.get(key)
        if not y or y.get('private'):
            return None
        if 'jump' in y and y['jump']:
            ox = key
            key = y['jump']
            y = self.channel_data.get(key)
            if not y or y.get('private'):
                return None
                # print(ox, x)
        return y['pid']

    def load_meta_data(self):
        with open(self.meta_data_path) as fh:
            self.channel_data = cPickle.load(fh)
            self.channel_pid_data = {x['pid']: x for x in self.channel_data.itervalues()}

    def save_index_data(self):
        assert self.channel_cid2idx and self.channel_cid2idx
        channel_index = {'cid2idx': self.channel_cid2idx, 'idx2cid': self.channel_idx2cid}
        with open(self.index_data_path, 'w') as fh:
            cPickle.dump(channel_index, fh)

    def load_index_data(self):
        with open(self.index_data_path) as fh:
            channel_idx_data = cPickle.load(fh)
            self.channel_cid2idx = channel_idx_data['cid2idx']
            self.channel_idx2cid = channel_idx_data['idx2cid']


USER_SUBS_COLUMNS = ['cn', 'lang', 'br', 'cs']
EVST_USER_SUBS_COLUMNS = ['uid', 'cs']


def _dump_user_subs(channel_helper, output, max_subs=1000):
    rs0 = TCastBoxInstallation.find()
    rs1 = TEverestInstallation.find()
    rs = itertools.chain(*[rs0, rs1])
    fh = open(output, 'w')
    rec_count = 0
    docs = []
    for r in rs:
        country = r.get('country')
        lang = r.get('language')
        brand = r.get('brand')
        channels = r.get('channels', [])
        cids = [channel_helper.key_to_pid(x) for x in channels]
        # print(channels, cids)
        cids = [x for x in cids if x]
        cids = list(set(cids))
        if not cids: continue
        # 如果超过1k的话，那么认为这个用户有点滥用
        if len(cids) > max_subs: continue
        cids.sort()
        cs = '+'.join(map(str, cids))
        docs.append({'cn': country, 'lang': lang, 'br': brand, 'cs': cs})
        rec_count += 1
        # 10w batch size 输出
        if (rec_count % 100000) == 0:
            print(rec_count)
            df = pd.DataFrame.from_records(docs)
            df.to_csv(fh, columns=USER_SUBS_COLUMNS, index=False, header=False)
            docs = []
    if docs:
        print(rec_count)
        df = pd.DataFrame.from_records(docs)
        df.to_csv(fh, columns=USER_SUBS_COLUMNS, index=False, header=False)
        docs = []
    fh.close()


def _dump_evst_user_subs(channel_helper, output, max_subs=1000):
    rs = TUserData.find()
    fh = open(output, 'w')
    rec_count = 0
    docs = []
    for r in rs:
        uid = r.get('uid')
        sub_channels = r.get('sub_channels', [])
        cids = [channel_helper.key_to_pid(x.get('channel_id')) for x in sub_channels]
        cids = [x for x in cids if x]
        cids = list(set(cids))
        # 支持输出空订阅的用户
        if not cids: continue
        # 如果超过1k的话，那么认为这个用户有点滥用
        if len(cids) > max_subs: continue
        cids.sort()
        cs = '+'.join(map(str, cids))
        docs.append({'uid': uid, 'cs': cs})
        rec_count += 1
        # 10w batch size 输出
        if (rec_count % 100000) == 0:
            print(rec_count)
            df = pd.DataFrame.from_records(docs)
            df.to_csv(fh, columns=EVST_USER_SUBS_COLUMNS, index=False, header=False)
            docs = []
    if docs:
        print(rec_count)
        df = pd.DataFrame.from_records(docs)
        df.to_csv(fh, columns=EVST_USER_SUBS_COLUMNS, index=False, header=False)
        docs = []
    fh.close()


def get_channel_subs(subs_df):
    cs = subs_df['cs']
    subs = defaultdict(int)
    count = 0
    for x in mytqdm(cs):
        count += 1
        # if count % 500000 == 0:
        #     print(count)
        try:
            _x = map(int, x.split('+'))
        except Exception:
            print(x)
            continue
        # 如果一个用户订阅数量超过500个不考虑
        # 可能是个非典型用户或者是机器人
        if len(_x) > 500:
            continue
        for _c in _x:
            subs[_c] += 1
    return subs


class UserHelper:
    def __init__(self, channel_helper):
        self.channel_helper = channel_helper
        self.subs_data_path = DATA_DIR + 'user_subs.csv'
        self.evst_subs_data_path = DATA_DIR + 'evst_user_subs.csv'
        self.subs_idx_data_path = DATA_DIR + 'user_subs_idx.csv'
        self.evst_subs_idx_data_path = DATA_DIR + 'evst_user_subs_idx.csv'
        self.locale_data_path = DATA_DIR + 'user_locale.data'
        self.evst_user_email_data_path = DATA_DIR + 'evst_user_email.csv'
        self.locales = None
        self.locale_index = None

    # ==================================
    def save_locale_data(self, locales):
        assert locales is not None
        with open(self.locale_data_path, 'w') as fh:
            cPickle.dump(locales, fh)

    def load_locale_data(self):
        with open(self.locale_data_path) as fh:
            locales = cPickle.load(fh)
            self.locales = locales
            self.locale_index = {locale: idx for (idx, locale) in enumerate(locales)}

    def get_locale_code(self, locale):
        return self.locale_index.get(locale, len(self.locales))

    # ==================================
    def dump_subs(self):
        _dump_user_subs(self.channel_helper, self.subs_data_path)

    def dump_evst_subs(self):
        _dump_evst_user_subs(self.channel_helper, self.evst_subs_data_path)

    def load_subs_df(self):
        return pd.read_csv(self.subs_data_path, names=USER_SUBS_COLUMNS)

    def load_evst_subs_df(self):
        return pd.read_csv(self.evst_subs_data_path, names=EVST_USER_SUBS_COLUMNS)

    # ==================================
    def save_subs_idx_df(self, subs_idx_df):
        assert subs_idx_df is not None
        subs_idx_df.to_csv(self.subs_idx_data_path, index=False, header=True)

    def save_evst_subs_idx_df(self, evst_subs_idx_df):
        assert evst_subs_idx_df is not None
        evst_subs_idx_df.to_csv(self.evst_subs_idx_data_path, index=False, header=True)

    def load_subs_idx_df(self):
        return pd.read_csv(self.subs_idx_data_path)

    def load_evst_subs_idx_df(self):
        return pd.read_csv(self.evst_subs_idx_data_path)

    # ===================================
    def pick_decent_channels(self, channel_subs):
        # 订阅数量小于10的channel不考虑，过于小众没有办法协同
        decent_channels = set(map(lambda x: x[0], filter(lambda x: x[1] >= 10, channel_subs.items())))
        print('# of decent channels = {}'.format(len(decent_channels)))
        channel_cid2idx = {}
        channel_idx2cid = []
        for i, cid in enumerate(list(decent_channels)):
            channel_cid2idx[cid] = i
            channel_idx2cid.append(cid)
        self.channel_helper.channel_cid2idx = channel_cid2idx
        self.channel_helper.channel_idx2cid = channel_idx2cid
        self.channel_helper.save_index_data()

    def make_idx_df(self, df):
        def _f(_xcs):
            xcs = filter(lambda x: x in self.channel_helper.channel_cid2idx, map(int, _xcs.split('+')))
            cids = [self.channel_helper.channel_cid2idx[x] for x in xcs]
            cids.sort()
            return '+'.join(map(str, cids))

        df2 = df.copy()
        df2['cs'] = df2['cs'].apply(_f)
        return df2

    # ======================================
    def dump_evst_user_email(self):
        rs = TEverestUser.find()
        docs = []
        for r in rs:
            uid = r.get('uid')
            auth_data = r.get('auth_data', {})
            email = None
            for k in ('google', 'facebook', 'twitter', 'email'):
                email = auth_data.get(k, {}).get('email')
                if email:
                    break
            if email:
                docs.append({'uid': uid, 'email': email})
                if len(docs) % 100000 == 0:
                    print('# of docs = {}'.format(len(docs)))
        df = pd.DataFrame.from_records(docs)
        df.to_csv(self.evst_user_email_data_path, columns=['uid', 'email'], index=False, header=True)

    def load_evst_user_email(self):
        return pd.read_csv(self.evst_user_email_data_path)


def build_coo_matrix(df, channel_helper):
    cs = df['cs']
    user_id = 0
    user_ids = []
    item_ids = []
    data = []
    for idx, _xcs in mytqdm(enumerate(cs)):
        if not _xcs or _xcs is np.nan:
            cids = []
        else:
            cids = map(int, _xcs.split('+'))
        for cid in cids:
            user_ids.append(user_id)
            item_ids.append(cid)
            data.append(1)
        user_id += 1
    coo_matrix = scipy.sparse.coo_matrix((data, (user_ids, item_ids)),
                                         shape=(user_id, len(channel_helper.channel_idx2cid)),
                                         dtype=np.float32)
    return coo_matrix


def build_train_matrix(mat_csr, n_users, min_subs=6, max_subs=20, random_state=42):
    np.random.seed(random_state)
    subs = np.array(np.sum(mat_csr, axis=1)).ravel()
    users_idx = np.arange(mat_csr.shape[0])
    print('# of all users = {}'.format(users_idx.shape[0]))
    ok_users_idx = users_idx[(subs <= max_subs) & (subs >= min_subs)]
    print('# of ok users = {}'.format(ok_users_idx.shape[0]))
    train_users_idx = np.random.choice(ok_users_idx, n_users, replace=False)
    print('# of train users = {}'.format(train_users_idx.shape[0]))

    train_rc = []
    row_idx = 0
    for row in mytqdm(train_users_idx):
        cols = mat_csr[row].indices
        train_rc.extend([(row_idx, x) for x in cols])
        row_idx += 1
    mat_coo = scipy.sparse.coo_matrix((np.ones(len(train_rc), dtype=np.float32),
                                       ([x[0] for x in train_rc], [x[1] for x in train_rc])),
                                      shape=(train_users_idx.shape[0], mat_csr.shape[1]),
                                      dtype=np.float32)
    mat_csr = mat_coo.tocsr()
    return mat_csr, train_users_idx


def train_test_split(mat_csr, n_test_users, random_state=42):
    np.random.seed(random_state)
    train_users_idx = np.arange(mat_csr.shape[0])
    test_users_idx = np.random.choice(train_users_idx, n_test_users, replace=False)
    print('# of test users = {}'.format(test_users_idx.shape[0]))

    test_rc = []
    for row in mytqdm(test_users_idx):
        cols = mat_csr[row].indices
        np.random.shuffle(cols)
        input_size = len(cols) / 2
        train_cols = cols[:input_size]
        test_cols = cols[input_size:]
        test_rc.extend([(row, x) for x in test_cols])
    test_mat_coo = scipy.sparse.coo_matrix((np.ones(len(test_rc), dtype=np.float32),
                                            ([x[0] for x in test_rc], [x[1] for x in test_rc])),
                                           shape=mat_csr.shape, dtype=np.float32)
    test_mat_csr = test_mat_coo.tocsr()
    train_mat_csr = mat_csr - test_mat_csr
    return train_mat_csr, test_mat_csr, test_users_idx


class MyLightFM(LightFM):
    def __init__(self, **kwargs):
        LightFM.__init__(self, **kwargs)
        self.epoch_number = 0
        self.fit_callback = None

    def _run_epoch(self, item_features, user_features, interactions, sample_weight, num_threads, loss):
        start_time = time.time()
        LightFM._run_epoch(self, item_features, user_features, interactions, sample_weight, num_threads, loss)
        end_time = time.time()
        if self.fit_callback:
            self.fit_callback(self.epoch_number, end_time - start_time)
        print('Epoch {} in {:.2f}s'.format(self.epoch_number, end_time - start_time))
        self.epoch_number += 1
