#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import pandas as pd
import numpy as np
import sklearn
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.base import BaseEstimator, RegressorMixin

df = pd.read_csv('mytrain.csv')
test_df = pd.read_csv('mytest.csv')
X, y = df.drop(['casual', 'registered', 'count'], axis = 1), np.log1p(df[['casual', 'registered', 'count']])

def input_fn(x, casual = True):
    drop_fields = ['dt_day', 'dt_hour', 'season', 'weather', 'dt_year', 'dt_month', 'dt_weekday', 'atemp']
    if 'datetime' in x.columns:
        drop_fields.append('datetime')
    return x.drop(drop_fields, axis = 1)

def rmse(x, y):
    return mean_squared_error(x, y) ** 0.5

def make_cv(X,n = 2):
    for i in range(n):
        days = [x for x in [18-i, 19-i]]
        train_idx = X[X['dt_day'].apply(lambda x: x not in days)].index
        test_idx = X[X['dt_day'].apply(lambda x: x in days)].index
        yield train_idx, test_idx

class MyEstimator(BaseEstimator, RegressorMixin):
    def __init__(self, **kwargs):
        if 'ma' in kwargs:
            self.ma = kwargs['ma']
            del kwargs['ma']
        if 'mb' in kwargs:
            self.mb = kwargs['mb']
            del kwargs['mb']
        kwargs['init'] = True
        self.set_params(**kwargs)

    def fit(self, X, y):
        input_a = input_fn(X, casual=True)
        input_b = input_fn(X, casual=False)
        self.ma.fit(input_a, y['casual'])
        self.mb.fit(input_b, y['registered'])
        self.ca = input_a.columns
        self.cb = input_b.columns

    def predict(self, X):
        ya = self.ma.predict(input_fn(X, casual=True))
        yb = self.mb.predict(input_fn(X, casual=False))
        y = np.log1p(np.expm1(ya) + np.expm1(yb))
        return y

    def score(self, X, y):
        y2 = self.predict(X)
        return -rmse(y['count'], y2)

    def set_params(self, **params):
        pa = {}
        pb = {}
        for k in params:
            if k.startswith('a_'):
                pa[k[2:]] = params[k]
            elif k.startswith('b_'):
                pb[k[2:]] = params[k]
            elif k == 'n_estimators':
                # 让两个回归器共享n
                pa[k] = params[k]
                pb[k] = params[k]
            else:
                pass
        if 'init' not in params:
            #print(pa, pb)
            pass
        self.ma.set_params(**pa)
        self.mb.set_params(**pb)
        return self

    def get_params(self, deep = True):
        pa = self.ma.get_params(deep)
        pb = self.ma.get_params(deep)
        p = {}
        for k in pa:
            p['a_' + k] = pa[k]
        for k in pb:
            p['b_' + k] = pb[k]
        p['ma'] = self.ma
        p['mb'] = self.mb
        return p

# ============================================================
# RF Model
print('cv for rf model')
rf0 = RandomForestRegressor(n_estimators=200, random_state = 42, verbose=0, n_jobs=4)
rf1 = RandomForestRegressor(n_estimators=200, random_state = 42, verbose=0, n_jobs=4)
rf = MyEstimator(ma = rf0, mb = rf1)
rf_best_params = {'a_min_samples_split': 10, 'b_min_samples_split': 7, 'n_estimators': 1700}
rf.set_params(**rf_best_params)
rf.fit(X, y)
output_y = rf.predict(test_df)
output = np.round(np.expm1(output_y)).astype(int)
output[output < 0] = 0
df_output = pd.DataFrame({'datetime': test_df['datetime'], 'count': output}, columns=('datetime', 'count'))
df_output['count'] = df_output['count'].astype(int)
df_output.to_csv('submission-rf.csv', index = False)

#============================================================
# GBM Model
print('cv for gbm model')
gbm0 = GradientBoostingRegressor(n_estimators=200, random_state = 42, verbose=0)
gbm1 = GradientBoostingRegressor(n_estimators=200, random_state = 42, verbose=0)
gbm = MyEstimator(ma = gbm0, mb = gbm1)
gbm_best_params = {'a_max_depth': 4, 'b_max_depth':6, 'n_estimators': 360}
gbm.set_params(**gbm_best_params)
gbm.fit(X, y)
output_y = gbm.predict(test_df)
output = np.round(np.expm1(output_y)).astype(int)
output[output < 0] = 0
df_output = pd.DataFrame({'datetime': test_df['datetime'], 'count': output}, columns=('datetime', 'count'))
df_output['count'] = df_output['count'].astype(int)
df_output.to_csv('submission-gbm.csv', index = False)

#============================================================
# XGB Model. 本质上这个和GBM是一个模型，最后得到的最佳参数都是一致的。
print('cv for xgb model')
from xgboost import XGBRegressor
xgb0 = XGBRegressor(n_estimators=200, random_state = 42, verbose=0, n_jobs=4)
xgb1 = XGBRegressor(n_estimators=200, random_state = 42, verbose=0, n_jobs=4)
xgb = MyEstimator(ma = xgb0, mb = xgb1)
xgb_best_params = {'a_max_depth': 5, 'b_max_depth':4, 'n_estimators': 925}
xgb.set_params(**xgb_best_params)
xgb.fit(X, y)
output_y = xgb.predict(test_df)
output = np.round(np.expm1(output_y)).astype(int)
output[output < 0] = 0
df_output = pd.DataFrame({'datetime': test_df['datetime'], 'count': output}, columns=('datetime', 'count'))
df_output['count'] = df_output['count'].astype(int)
df_output.to_csv('submission-xgb.csv', index = False)

#============================================================
# Average All
df_rf = pd.read_csv('submission-rf.csv')
df_gbm = pd.read_csv('submission-gbm.csv')
df_xgb = pd.read_csv('submission-xgb.csv')
df_avg = pd.DataFrame(df_rf)
df_avg['count'] = np.round((df_rf['count'] + df_gbm['count'] + df_xgb['count'] + 1) * 0.33).astype(int)
df_avg.to_csv('submission.csv', index = False)
