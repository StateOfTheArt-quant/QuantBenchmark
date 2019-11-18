#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import pandas as pd
import numpy as np

from quant_benchmark.model_train.model_train import training

class ModelTrain(unittest.TestCase):
    
    def test_training(self):

        d = {}
        for i in ["000001.XSHE","000002.XSHE","000016.XSHE","000008.XSHE"]: 
            d[i] = pd.DataFrame(np.random.randn(100,6), columns=["EP","BP","ROCP","MACD","RSI6","Label"], index=pd.date_range('2019-01-01 00:00:00', periods=100)) # 100天
        data_df = pd.concat(d)
        data_df.index.names = ["order_book_id", "datetime"]
        print(data_df) 
    
        lr_coef_df, lasso_coef_df, rr_coef_df, en_coef_df = training(data_df)
        print("ols Regression coef: \n", lr_coef_df)
        print("lasso regression coef: \n", lasso_coef_df)
        print("Ridge regression coef: \n",rr_coef_df)
        print("ElasticNet regression coef: \n", en_coef_df)


if __name__ == "__main__":
    
    unittest.main()