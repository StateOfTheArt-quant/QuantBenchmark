#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import pandas as pd
import numpy as np

from quant_benchmark.model_train.trainer import Trainer
from quant_benchmark.model.sklearn_models import lasso, skols

class ModelTrain(unittest.TestCase):
    
    def setUp(self):
        d = {}
        for i in ["000001.XSHE","000002.XSHE","000016.XSHE","000008.XSHE"]: 
            d[i] = pd.DataFrame(np.random.randn(100,6), columns=["EP","BP","ROCP","MACD","RSI6","Label"], index=pd.date_range('2019-01-01 00:00:00', periods=100)) # 100天
        data_df = pd.concat(d)
        data_df.index.names = ["order_book_id", "datetime"]
        self.data = data_df
    
    def test_sklearn_trainer_1(self):
        model = lasso()
        trainer = Trainer(model)
        coef_df, r2 = trainer.sklearn_trainer(self.data, label_name="Label")
        print("lasso coef:\n", coef_df)
        print("lasso r2 score:\n", r2)
        
    def test_sklearn_trainer_2(self):
        model = skols()
        trainer = Trainer(model)
        coef_df, r2 = trainer.sklearn_trainer(self.data, label_name="Label")
        print("linear regression coef:\n", coef_df)
        print("linear regression r2 score:\n", r2)


if __name__ == "__main__":
    
    unittest.main()