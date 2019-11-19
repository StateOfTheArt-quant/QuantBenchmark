#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from quant_benchmark.data.base_data_source.default_data_source import DefaultDataSource

import jqdatasdk
#see https://github.com/JoinQuant/jqdatasdk/blob/master/tests/test_api.py
jqdatasdk.auth(username='13922819479', password='123456')


data_source = DefaultDataSource()

order_book_id = "000001.XSHE"
bar_count = 10
dt = "2019-09-20"

data = data_source.history_bars(order_book_id=order_book_id, bar_count=bar_count, frequency="1w", dt=dt)

