#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# QSTK Imports
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def get_close_price(dt_start, dt_end, ls_symbols):
    dt_timeofday = dt.timedelta(hours=16)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
    c_dataobj = da.DataAccess('Yahoo')
    ls_keys = ['close']
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(list(zip(ls_keys, ldf_data)))

    # Filling the data for NAN
    for s_key in ls_keys:
        d_data[s_key] = d_data[s_key].fillna(method='ffill')
        d_data[s_key] = d_data[s_key].fillna(method='bfill')
        # d_data[s_key] = d_data[s_key].fillna(1.0)  # never exec.?

    na_price = d_data['close'].values
    df_price = pd.DataFrame(
        na_price, index=ldt_timestamps, columns=ls_symbols)
    return df_price


def test_data():
    dt_start = dt.datetime(2010, 1, 1)
    dt_end = dt.datetime(2010, 12, 31)
    df_price = get_close_price(
        dt_start, dt_end, ['AAPL', 'GOOG', 'IBM', 'MSFT', 'VZ'])
    return df_price


def bollinger_band(df_price, lookback=20, times=1):
    df_mean = pd.rolling_mean(df_price, 20)
    df_std = pd.rolling_std(df_price, 20)
    df_bb_ratio = (df_price - df_mean) / (times * df_std)
    df_high = df_mean + times * df_std
    df_low = df_mean - times * df_std
    return (df_mean, df_high, df_low, df_bb_ratio)


def plot_bollinger_band(df_price, df_mean, df_high, df_low, df_bb_ratio, prefix):
    for sym in df_price.columns:
        plt.clf()
        fig, (ax1, ax2) = plt.subplots(2, 1)
        ax1.plot(df_price[sym], label=sym)
        ax1.plot(df_mean[sym], label='rolling mean')
        ax1.plot(df_low[sym], color='#a0a0a0')
        ax1.plot(df_high[sym], color='#a0a0a0')
        ax1.fill_between(np.arange(len(df_low)), df_low[
                         sym], df_high[sym], facecolor='#e0e0e0', alpha=0.5)
        ax1.set_ylabel('Adjusted Close')
        ax1.legend(loc='best')

        ax2.plot(df_bb_ratio[sym])
        ymin, ymax = ax2.get_ylim()
        ax2.axvspan(0, len(df_low) - 1, ymin=(-1.0 - ymin) / (ymax - ymin),
                    ymax=(1.0 - ymin) / (ymax - ymin), facecolor='#e0e0e0', alpha=0.5)
        ax2.set_ylabel('Bollinger Feature')

        def plot_peak(ax, ro):
            sz = ro.shape[0]
            peaks = []
            for (idx, r) in enumerate(ro):
                peak = False
                if r >= 1.0:
                    if (idx > 0 and r > ro[idx - 1]) and \
                            (idx < (sz - 1) and r > ro[idx + 1]):
                        peak = True
                if r <= -1.0:
                    if (idx > 0 and r < ro[idx - 1]) and \
                            (idx < (sz - 1) and r < ro[idx + 1]):
                        peak = True
                if peak:
                    # local peak
                    peaks.append((idx, r))
            # get global peaks.
            for (i, p) in enumerate(peaks):
                ax.axvline(p[0], color='g')
        plot_peak(ax1, df_bb_ratio[sym])
        plot_peak(ax2, df_bb_ratio[sym])
        plt.savefig('%s-%s.pdf' % (prefix, sym), format='pdf')


if __name__ == '__main__':
    df_price = test_data()
    (m, h, l, r) = bollinger_band(df_price, times=2)
    plot_bollinger_band(df_price, m, h, l, r, 'hw5')
    print r[80:120]
