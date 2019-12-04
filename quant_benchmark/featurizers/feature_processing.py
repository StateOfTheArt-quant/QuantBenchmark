#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# ======================================================================================= #
#  workflow to data preprocessing                                                         #
#    1 异常值处理 （防止异常值改变整体的均值和方差）                                        #
#        1.1 df.replace([-np.inf, np.inf], np.nan)                                        #
#        1.2 winsorize                                                                    #
#    2 标准化处理  （关键在于对nan的处理，计算均值时不考虑nan, sklearn.fit 可以做到 ）      #
#    3 fillna_or_dropna                                                                   #
#    4 add industry_dummy+variable(optional)                                              #
# ======================================================================================= #

# ================================================================================ #
#  1 winsorize for dataframe all columns                                           #
# ================================================================================ #
def winsorize_series(series: pd.Series, lower_bound: float = 0.01, upper_bound: float = 0.99) -> pd.Series:
    """limit the extrem value between lower_bound and upper_bound"""
    assert isinstance(series, pd.Series), "shold be pd.Series"
    quantile_dist = series.quantile([lower_bound, upper_bound])      
    series[series < quantile_dist.iloc[0]] = quantile_dist.iloc[0]
    series[series > quantile_dist.iloc[1]] = quantile_dist.iloc[1]
    return series

def winsorize_df(dataframe : pd.DataFrame, lower_bound: float = 0.01, upper_bound: float = 0.99) -> pd.DataFrame:
    """limit the extrem value between lower_bound and upper_bound"""
    assert isinstance(dataframe, pd.DataFrame), "should be a pd.Dataframe"
    return dataframe.apply(lambda x:winsorize_series(x, lower_bound, upper_bound))

def winsorizer(dataframe : pd.DataFrame, lower_bound: float = 0.01, upper_bound: float = 0.99) -> pd.DataFrame:
    """limit the extrem value between lower_bound and upper_bound"""
    assert isinstance(dataframe, pd.DataFrame), "should be a pd.Dataframe"
    return dataframe.groupby(level=1).apply(winsorize_df, lower_bound=lower_bound, upper_bound=upper_bound)

# =================================================================== #
#  2 standardlize feature                                             #
# =================================================================== #
def standardlize_df(df: pd.DataFrame) -> pd.DataFrame:
    scaler = StandardScaler()
    df = pd.DataFrame(scaler.fit_transform(df), index=df.index, columns=df.columns)    
    return df

def standardlizer(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(level=1).apply(standardlize_df)



def preprocess_raw_feature(df: pd.DataFrame, lower_bound: float=0.01, upper_bound: float=0.99) -> pd.DataFrame:
    # =================================================== #
    # 1 winsorize the anormaly                            #
    # =================================================== #
    df = df.replace([-np.inf, np.inf], np.nan)
    df = winsorizer(df, lower_bound=lower_bound, upper_bound=upper_bound)
    
    # =================================================== #
    # 2 dropna                                            #
    # =================================================== #
    df = df.dropna(axis=0, thresh=int(df.shape[1]*0.5))

    # =================================================== #
    # 3 standardlize with nan                             #
    # =================================================== #
    df = standardlizer(df)
    
    # =================================================== #
    # 4 fillna                                            #
    # =================================================== #
    df = df.fillna(0)
    
    # =================================================== #
    # 5 optional add industry dummy variable              #
    # =================================================== #
    return df
