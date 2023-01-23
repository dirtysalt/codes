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


def simulate(orders, amount):
    dt_timeofday = dt.timedelta(hours=16)
    dt_start = orders[0][0]
    dt_end = orders[-1][0]
    # print(dt_start, dt_end)
    ls_symbols = list(set([x[1] for x in orders]))
    dt_timeofday = dt.timedelta(hours=16)
    ldt_timestamps = du.getNYSEdays(
        dt_start, dt_end + dt.timedelta(hours=24), dt_timeofday)
    c_dataobj = da.DataAccess('Yahoo')
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ['close'])
    df_price = ldf_data[0]
    cash = amount
    stocks = {}
    values = []
    order_idx = 0
    for ts in ldt_timestamps:
        date = dt.datetime(ts.year, ts.month, ts.day)
        while order_idx < len(orders) and orders[order_idx][0] == date:
            o = orders[order_idx]
            (_, sym, direction, qty) = o
            price = df_price[sym].ix[ts]
            if direction == 'Buy':
                cash -= price * qty
                if sym in stocks:
                    stocks[sym] += qty
                else:
                    stocks[sym] = qty
            else:
                cash += price * qty
                if sym in stocks:
                    stocks[sym] -= qty
                else:
                    stocks[sym] = -qty
            order_idx += 1
        total = cash
        for sym in list(stocks.keys()):
            qty = stocks[sym]
            price = df_price[sym].ix[ts]
            total += qty * price
        values.append(total)
    return (ldt_timestamps, np.array(values))


def compare_to_SPX(ldt_timestamps, values, output_pdf='hw3.pdf'):
    c_dataobj = da.DataAccess('Yahoo')
    ldf_data = c_dataobj.get_data(ldt_timestamps, ['$SPX'], ['close'])
    spx_values = ldf_data[0].values
    values = np.expand_dims(values, axis=1)
    prices = np.hstack((values, spx_values))
    na_normalized_prices = prices / prices[0, :]

    def stock_stat(prices):
        na_rets = tsu.returnize0(prices)
        N = 252
        std = np.std(na_rets, axis=0)
        mean = np.mean(na_rets, axis=0)
        sr = np.sqrt(N) * mean / std
        total = np.cumprod(na_rets + 1, axis=0)[-1, :]
        return (std, mean, sr, total)

    (std, mean, sr, total) = stock_stat(na_normalized_prices)
    print('Date Range: %s to %s' % (ldt_timestamps[0], ldt_timestamps[-1]))
    print('Sharpe Ratio of Fund and $SPX: %s' % (sr))
    print('Total Return of Fund and $SPX: %s' % (total))
    print('Standard Deviation of Fund and $SPX: %s' % (std))
    print('Average Daily Return of Fund and $SPX: %s' % (mean))

    plt.clf()
    N = na_normalized_prices.shape[0]
    plt.plot(np.arange(N), na_normalized_prices)
    plt.legend(['Fund', '$SPX'], loc='upper left')
    plt.ylabel('Normalized Prices')
    plt.xlabel('Time')
    plt.savefig(output_pdf, format='pdf')


def read_orders(fname):
    with open(fname) as fh:
        orders = []
        for s in fh:
            (year, mon, day, sym, direction, qty, _) = s.strip().split(',')
            date = dt.datetime(int(year), int(mon), int(day))
            orders.append((date, sym, direction, int(qty)))
        orders.sort(lambda x, y: cmp(x[0], y[0]))
        # print orders
        return orders


def output_values(ldt_timestamps, values):
    rs = list(zip(ldt_timestamps, values))
    lines = ['%d,%d,%d,%d' %
                (x[0].year, x[0].month, x[0].day, x[1]) for x in rs]
    for x in lines:
        print(x)

if __name__ == '__main__':
    # orders = read_orders('orders-short.csv')
    # orders = read_orders('orders.csv')
    orders = read_orders('orders2.csv')
    (ldt_timestamps, values) = simulate(orders, 1000000)
    output_values(ldt_timestamps, values)
    compare_to_SPX(ldt_timestamps, values)
