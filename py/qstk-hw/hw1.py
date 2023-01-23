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


def stock_price(dt_start, dt_end, ls_symbols):
    # We need closing prices so the timestamp should be hours=16.
    dt_timeofday = dt.timedelta(hours=16)

    # Get a list of trading days between the start and the end.
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

    # Creating an object of the dataaccess class with Yahoo as the source.
    # c_dataobj = da.DataAccess('Yahoo', cachestalltime = 0)
    c_dataobj = da.DataAccess('Yahoo')

    # Keys to be read from the data, it is good to read everything in one go.
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    # Reading the data, now d_data is a dictionary with the keys above.
    # Timestamps and symbols are the ones that were specified before.
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(list(zip(ls_keys, ldf_data)))

    # Filling the data for NAN
    for s_key in ls_keys:
        d_data[s_key] = d_data[s_key].fillna(method='ffill')
        d_data[s_key] = d_data[s_key].fillna(method='bfill')
        # d_data[s_key] = d_data[s_key].fillna(1.0)  # never exec.?

    na_price = d_data['close'].values
    na_normalized_price = na_price / na_price[0, :]
    return na_normalized_price


def stock_stat(na_normalized_price, lf_port_alloc):
    na_port_price = np.sum(na_normalized_price * lf_port_alloc, axis=1)
    na_rets = tsu.returnize0(na_port_price)
    # N = na_rets.size
    N = 252
    std = np.std(na_rets)
    mean = np.mean(na_rets)
    sr = np.sqrt(N) * mean / std
    total = np.cumprod(na_rets + 1)[-1]
    return (mean, std, sr, total)


def simulate(dt_start, dt_end, symbols, port_alloc):
    price = stock_price(dt_start, dt_end, symbols)
    stat = stock_stat(price, port_alloc)
    return stat


def simulate_year(year, symbols, port_alloc):
    dt_start = dt.datetime(year, 1, 1)
    dt_end = dt.datetime(year, 12, 31)
    stat = simulate(dt_start, dt_end, symbols, port_alloc)
    return stat

import itertools


def test_simulate():
    S = """Start Date: January 1, 2011
End Date: December 31, 2011
Symbols: ['AAPL', 'GLD', 'GOOG', 'XOM']
Optimal Allocations: [0.4, 0.4, 0.0, 0.2]
Sharpe Ratio: 1.02828403099
Volatility (stdev of daily returns):  0.0101467067654
Average Daily Return:  0.000657261102001
Cumulative Return:  1.16487261965

Start Date: January 1, 2010
End Date: December 31, 2010
Symbols: ['AXP', 'HPQ', 'IBM', 'HNZ']
Optimal Allocations:  [0.0, 0.0, 0.0, 1.0]
Sharpe Ratio: 1.29889334008
Volatility (stdev of daily returns): 0.00924299255937
Average Daily Return: 0.000756285585593
Cumulative Return: 1.1960583568"""

    ls_symbols = ['AAPL', 'GLD', 'GOOG', 'XOM']
    lf_port_alloc = [0.4, 0.4, 0.0, 0.2]
    stat = simulate_year(2011, ls_symbols, lf_port_alloc)
    assert(
        np.allclose(stat, (0.000657261102001, 0.0101467067654, 1.02828403099, 1.16487261965)))

    ls_symbols = ['AXP', 'HPQ', 'IBM', 'HNZ']
    lf_port_alloc = [0.0, 0.0, 0.0, 1.0]
    stat = simulate_year(2010, ls_symbols, lf_port_alloc)
    assert(
        np.allclose(stat, (0.000756285585593, 0.00924299255937, 1.29889334008, 1.1960583568)))


def search_best_port(na_normalized_price):
    pr = np.arange(0, 1.00001, 0.1)
    best = [0, None]

    def check(p):
        stat = stock_stat(na_normalized_price, p)
        (mean, std, sr, total) = stat
        # print(sr, std)
        if not best[0] or sr > best[0]:
            best[0] = sr
            best[1] = p

    for p0 in pr:
        for p1 in pr:
            for p2 in pr:
                if (p0 + p1 + p2) > 1.0:
                    continue
                p = [p0, p1, p2, 1.0 - p0 - p1 - p2]
                check(p)
    return best


def find_best_port(year, ls_symbols):
    dt_start = dt.datetime(year, 1, 1)
    dt_end = dt.datetime(year, 12, 31)
    price = stock_price(dt_start, dt_end, ls_symbols)
    best_port = search_best_port(price)
    print('best port alloc = {}, sr = {}'.format(best_port[1], best_port[0]))
    best_port_alloc = best_port[1]
    best_port_price = np.sum(price * best_port_alloc, axis=1)
    return best_port_price


def homework():
    find_best_port(2011,  ['AAPL', 'GOOG', 'IBM', 'MSFT'])
    find_best_port(2010, ['BRCM', 'ADBE', 'AMD', 'ADI'])
    find_best_port(2011, ['BRCM', 'TXN', 'AMD', 'ADI'])
    find_best_port(2010, ['BRCM', 'TXN', 'IBM', 'HNZ'])
    find_best_port(2010, ['C', 'GS', 'IBM', 'HNZ'])
    find_best_port(2011, ['AAPL', 'GOOG', 'IBM', 'MSFT'])
    find_best_port(2011, ['BRCM', 'ADBE', 'AMD', 'ADI'])
    find_best_port(2011, ['BRCM', 'TXN', 'AMD', 'ADI'])
    find_best_port(2010,  ['BRCM', 'TXN', 'IBM', 'HNZ'])
    find_best_port(2010, ['C', 'GS', 'IBM', 'HNZ'])


def plot_performance(year, symbols, sp500):
    dt_start = dt.datetime(year, 1, 1)
    dt_end = dt.datetime(year, 12, 31)
    price_x = stock_price(dt_start, dt_end, [sp500])[:, 0]
    price_port = find_best_port(year, symbols)
    plt.clf()
    N = price_port.size
    plt.plot(np.arange(N), price_x)
    plt.plot(np.arange(N), price_port)
    plt.legend([sp500, 'my port'], loc='upper left')
    plt.ylabel('Normalized Price')
    plt.xlabel('Time')
    plt.savefig('hw1.pdf', format='pdf')

if __name__ == '__main__':
    test_simulate()
    plot_performance(2011, ['AAPL', 'GLD', 'GOOG', 'XOM'], 'SPY')
    homework()
