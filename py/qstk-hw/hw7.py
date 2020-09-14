#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


"""Back testing and Event Profile on Bollinger Band indicator"""

# QSTK Imports
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkstudy.EventProfiler as ep

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import copy
import hw3
import hw5
import hw4


def test_data():
    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    dataobj = da.DataAccess('Yahoo')
    ls_symbols = dataobj.get_symbols_from_list('sp5002012')
    ls_symbols.append('SPY')
    df_price = hw5.get_close_price(dt_start, dt_end, ls_symbols)
    return df_price


def event_study(df_price, bb_ratio, orders, study=None):
    bb_ratio_market = bb_ratio['SPY']
    print("Finding Events")
    df_events = copy.deepcopy(bb_ratio)
    df_events = df_events * np.NAN

    ldt_timestamps = bb_ratio.index
    ls_symbols = bb_ratio.columns

    for s_sym in ls_symbols:
        for i in range(1, len(ldt_timestamps)):
            ts = ldt_timestamps[i]
            yes_ts = ldt_timestamps[i - 1]
            if (bb_ratio[s_sym].ix[yes_ts] >= -2.0 and
                    bb_ratio[s_sym].ix[ts] <= -2.0 and
                    bb_ratio_market.ix[ts] >= 1.0):
                df_events[s_sym].ix[ts] = 1
                buy_ts = ts
                sell_idx = i + 5
                if sell_idx >= len(ldt_timestamps):
                    sell_ts = ldt_timestamps[-1]
                else:
                    sell_ts = ldt_timestamps[sell_idx]
                orders.append((buy_ts, s_sym, 'Buy', 100))
                orders.append((sell_ts, s_sym, 'Sell', 100))

    if study:
        print('Creating Study')
        ep.eventprofiler(df_events, {'close': df_price}, i_lookback=20, i_lookforward=20, s_filename='%s.pdf' % (
            study), b_market_neutral=True, b_errorbars=True, s_market_sym='SPY')
    return df_events


def main():
    df_price = test_data()
    (m, h, l, r) = hw5.bollinger_band(df_price)
    orders = []
    event_study(df_price, r, orders, 'hw7')
    hw4.write_orders(orders, 'hw7-orders.csv')
    orders = hw3.read_orders('hw7-orders.csv')
    (ldt_timestamps, values) = hw3.simulate(orders, 100000)
    hw3.compare_to_SPX(ldt_timestamps, values, 'hw7-compare-spx.pdf')

if __name__ == '__main__':
    main()
