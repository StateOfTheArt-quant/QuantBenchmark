#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score

def total_r2_score(y_true_np, y_hat_np):
    loss_error = 1-np.sum(np.square(y_true_np - y_hat_np))/np.sum(np.square(y_true_np))
    return loss_error

    
class Trainer(object):
    
    def __init__(self, model):
        self.model = model
        
    @staticmethod
    def split_Xy(df, label_name="Label"):
        assert label_name in df.columns 
        y = df[label_name]
        X = df[df.columns.drop(label_name)]
        return X, y
    
    def trainer(self, *args, **kwargs):
        pass
    
    
class SklearnTrainer(Trainer):
    
    def trainer(self, df, label_name="Label"):
        idx = df.columns.drop(label_name)
        coef_container = {}
        r2_container = {}
        for dt in df.index.levels[1]:
            print("cross regression on :", dt)
            df_dt = df.xs(dt, level=1)
            X, y = Trainer.split_Xy(df_dt, label_name=label_name)
            coef, relative_r2, total_r2 = self._sklearn_linear_regression(X, y)
            coef_container[dt] = coef
            r2_container[dt] = [relative_r2, total_r2]
        lr_coef_df = pd.DataFrame(coef_container, index=idx).transpose()
        r2_score = pd.DataFrame(r2_container, index=["relative_r2","total_r2"]).transpose()
        return lr_coef_df, r2_score       
    
    
    def _sklearn_linear_regression(self, X, y):
        self.model.fit(X, y)
        y_predict = self.model.predict(X)

        coef = self.model.coef_
        relative_r2 = r2_score(y, y_predict)
        total_r2 = total_r2_score(y, y_predict)
        print("relative r2 score: {}, total r2 score: {}".format(relative_r2, total_r2))
        return coef, relative_r2, total_r2
    
    
    
class DeepLearningTrainer(Trainer):
    
    def trainer(self):
        pass