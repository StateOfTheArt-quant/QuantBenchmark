#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

from sklearn.metrics import r2_score

from quant_benchmark.model_train.models import skols, enet_model, lasso, ridge


def _sklearn_train(X, y):
    
    lr = skols()
    ls = lasso()
    rr = ridge()
    en = enet_model(alpha=0.1, l1_ratio=0.7)
#    
##------------------LinearRegression--------------------------------
    print('--------lr----------')
    lr.fit(X, y)
    lr_predict = lr.predict(X)

    lr_coef = lr.coef_    
    r2 = r2_score(y, lr_predict)
    print("r2 score:", r2)
    
#    
##------------------LassoRegression--------------------------------
    print('--------lasso----------')
    ls.fit(X, y)
    ls_predict = ls.predict(X)
    
    lasso_coef = ls.coef_ 
    r2 = r2_score(y, ls_predict)
    print("r2 score:", r2)
    
#    
##------------------RidgeRegression--------------------------------
    print('--------ridge----------')
    rr.fit(X, y)
    rr_predict = rr.predict(X)

    rr_coef = rr.coef_ 
    r2 = r2_score(y, rr_predict)
    print("r2 score:", r2)

#
##------------------ElasticNet---------------------------------------
    print('--------en----------')
    en.fit(X, y)
    en_predict = en.predict(X)

    en_coef = en.coef_     
    r2 = r2_score(y, en_predict)
    print("r2 score:", r2)
    
    return lr_coef, lasso_coef, rr_coef, en_coef


def split_Xy(df):
    assert "Label" in df.columns 
    y = df["Label"]
    X = df[df.columns.drop("Label")]
    return X, y

def sklearn_train(df):
    X, y = split_Xy(df)
    return _sklearn_train(X, y)
    
def training(df):
    idx = df.columns.drop("Label")
    lr_coef_container = {}
    lasso_coef_container = {}
    rr_coef_container = {}
    en_coef_container = {}
    for dt in df.index.levels[1]:
        print(dt)
        df_dt = df.xs(dt, level="datetime")
        lr_coef, lasso_coef, rr_coef, en_coef = sklearn_train(df_dt)
        lr_coef_container[dt] = lr_coef
        lasso_coef_container[dt] = lasso_coef
        rr_coef_container[dt] = rr_coef
        en_coef_container[dt] = en_coef
    lr_coef_df = pd.DataFrame(lr_coef_container, index=idx).transpose()
    lasso_coef_df = pd.DataFrame(lasso_coef_container, index=idx).transpose()
    rr_coef_df = pd.DataFrame(rr_coef_container, index=idx).transpose()
    en_coef_df = pd.DataFrame(en_coef_container, index=idx).transpose()
    
    return lr_coef_df, lasso_coef_df, rr_coef_df, en_coef_df

