#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.ensemble import RandomForestRegressor


# sklearn ols
def skols(fit_intercept=True):
    return LinearRegression(fit_intercept=fit_intercept)

# sklearn lasso
def lasso(alpha=0.01):
    return Lasso(alpha=alpha)

# sklearn ridge
def ridge(alpha=0.5):
    return Ridge(alpha=alpha)

# ENet
def enet_model(alpha=0.1, l1_ratio=0.7):
    return ElasticNet(alpha=alpha, l1_ratio=l1_ratio)

# RandomForestRegressor
def rf_model():
    return RandomForestRegressor()


    