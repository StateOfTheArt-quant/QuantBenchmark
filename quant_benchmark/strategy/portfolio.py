#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

def predict_return(exposure:pd.DataFrame, factor_return:pd.Series) -> pd.Series:
    """
    exposure: index: order_book_id, columns: factor_name
    factor_return: index: factor_name
    """
    predicted = np.dot(exposure, factor_return)
    return pd.Series(predicted, index=exposure.index)


def long_short_portfolio(estimate_return:pd.Series, long_percent=0.1, short_percent=0.1):
    long_count = int(len(estimate_return)*long_percent) if len(estimate_return)*long_percent>0.5 else 1
    short_count = int(len(estimate_return)*short_percent) if len(estimate_return)*short_percent>0.5 else 1
    estimate_return = estimate_return.sort_values(ascending=False)
    long_portfolio = estimate_return[:long_count].index.to_list()
    short_portfolio = estimate_return[-short_count:].index.to_list()
    return long_portfolio, short_portfolio
    