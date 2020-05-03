#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import pandas as pd
import numpy as np
import xgboost
import sklearn
data_path = '/Users/dirlt/.kaggle/competitions/bike-sharing-demand/'

def extend_fields(df, as_float = False):
    df = df.copy()
    dt = df['datetime']
    dt2 = pd.to_datetime(dt)
    df['dt_day'] = dt2.apply(lambda x: x.day)
    df['dt_weekday'] = dt2.apply(lambda x: x.weekday())
    df['dt_month'] = dt2.apply(lambda x: x.month)
    df['dt_hour'] = dt2.apply(lambda x: x.hour)
    df['dt_year'] = dt2.apply(lambda x: x.year)
    x = df
    if not as_float:
        x['temp'] = np.round(x['temp']).astype(int)
        x['atemp'] = np.round(x['atemp']).astype(int)
        x['humidity'] = np.round(x['humidity']).astype(int)
        x['windspeed'] = np.round(x['windspeed']).astype(int)
    tmp = pd.get_dummies(x['season'], prefix = 'season')
    x = x.join(tmp)
    tmp = pd.get_dummies(x['weather'], prefix = 'weather')
    x = x.join(tmp)
    tmp = pd.get_dummies(x['dt_weekday'], prefix = 'weekday')
    x = x.join(tmp)
    tmp = pd.get_dummies(x['dt_month'], prefix = 'month')
    x = x.join(tmp)
    tmp = pd.get_dummies(x['dt_hour'], prefix = 'hour')
    x = x.join(tmp)
    tmp = pd.get_dummies(x['dt_year'], prefix = 'year')
    x = x.join(tmp)
    return x

def mark_windspeed(x):
    x['windspeed_0'] = 0
    x.loc[(x['windspeed'] == 0),'windspeed_0'] = 1
    return x

def mark_humidity(x):
    h = np.round(x['humidity']).astype(int)
    x['humidity_0'] = 0
    x.loc[h == 0, 'humidity_0'] = 1
    x['humidity_1'] = 0
    x.loc[(h >= 85) & (h <=92), 'humidity_1'] = 1
    x['humidity_2'] = 0
    x.loc[(h >92) & (h < 100), 'humidity_2'] = 1
    x['humidity_3'] = 0
    x.loc[h == 100, 'humidity_3'] = 1
    return x

def select_features(df, test = False):
    columns = ['holiday', 'workingday',  'casual', 'registered',
               'count', 'dt_month', 'dt_day', 'dt_hour',
               'temp', 'humidity', 'windspeed', 'atemp',
               'season', 'dt_weekday', 'weather', 'dt_year', 'windspeed_0',
               'humidity_0', 'humidity_1', 'humidity_2', 'humidity_3']
    columns.extend(['season_{}'.format(x) for x in range(1,5)])
    columns.extend(['weather_{}'.format(x) for x in range(1,5)])
    columns.extend(['weekday_{}'.format(x) for x in range(0, 7)])
    columns.extend(['month_{}'.format(x) for x in range(1, 13)])
    columns.extend(['year_{}'.format(x) for x in range(2011, 2013)])
    columns.extend(['hour_{}'.format(x) for x in range(0, 24)])

    if test:
        columns.remove('count')
        columns.remove('casual')
        columns.remove('registered')
        columns.insert(0, 'datetime')

    return df[columns]

train_df = pd.read_csv(data_path + 'train.csv')
train_df = extend_fields(train_df, as_float=True)
train_df = mark_windspeed(train_df)
train_df = mark_humidity(train_df)
output_df = select_features(train_df)
output_df.to_csv('mytrain.csv', index=False)

test_df = pd.read_csv(data_path + 'test.csv')
test_df = extend_fields(test_df, as_float=True)
test_df = mark_windspeed(test_df)
test_df = mark_humidity(test_df)
test_output_df = select_features(test_df, test=True)
test_output_df.to_csv('mytest.csv', index = False)
