#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import numpy as np
import pandas as pd

from quant_benchmark.featurizers.feature_creator import create_raw_feature
from quant_benchmark.featurizers.feature_processing import winsorizer, preprocess_raw_feature


class FeatureCreater(unittest.TestCase):
    
    def test_creat_raw_feature(self):
        raw_dict = {}
        for i in ["000001.XSHE","000002.XSHE","000016.XSHE","000008.XSHE"]: 
            raw_dict[i] = pd.DataFrame(np.random.randn(100,5), columns=["open","high","low","close","volume"], index=pd.date_range('2019-01-01 00:00:00', periods=100)) # 100天
        raw_df = pd.concat(raw_dict)    
        data = create_raw_feature(raw_df)
        print(data)
 
           
class FeatureProcessor(unittest.TestCase):
        
    def test_winsorizer(self):
        class1 = ["000001.XSHE","000001.XSHE","000002.XSHE","000002.XSHE","000002.XSHE","000016.XSHE","000016.XSHE","000016.XSHE"]
        class2 = [pd.Timestamp("2019-01-01"),pd.Timestamp("2019-01-02"),pd.Timestamp("2019-01-01"),pd.Timestamp("2019-01-02"),pd.Timestamp("2019-01-03"),pd.Timestamp("2019-01-01"),pd.Timestamp("2019-01-02"),pd.Timestamp("2019-01-03")]
        m_index = pd.MultiIndex.from_arrays([class1,class2],names=["order_book_id", "datetime"])        
        data_df = pd.DataFrame(np.random.randint(1,10,(8,3)),index=m_index, columns=["EP","BP","Label"])
        
        data_df["EP"].iloc[4] = 0
        data_df["EP"].iloc[7] = 10
        
        df = winsorizer(data_df, lower_bound=0.2, upper_bound=0.8)
        
        self.assertEqual(df["EP"].iloc[4], 2.0)
        self.assertEqual(df["EP"].iloc[7], 8.0)
        
    def test_preprocess_raw_feature(self):
        class1 = ["000001.XSHE","000001.XSHE","000002.XSHE","000002.XSHE","000002.XSHE","000016.XSHE","000016.XSHE","000016.XSHE"]
        class2 = [pd.Timestamp("2019-01-01"),pd.Timestamp("2019-01-02"),pd.Timestamp("2019-01-01"),pd.Timestamp("2019-01-02"),pd.Timestamp("2019-01-03"),pd.Timestamp("2019-01-01"),pd.Timestamp("2019-01-02"),pd.Timestamp("2019-01-03")]
        m_index = pd.MultiIndex.from_arrays([class1,class2],names=["order_book_id", "datetime"])
        data_df = pd.DataFrame(np.random.randint(1,10,(8,3)),index=m_index, columns=["EP","BP","Label"])
        
        data_df["EP"].iloc[1] = np.NAN
        
        df = preprocess_raw_feature(data_df, lower_bound=0.2, upper_bound=0.8)
        
        print(df)
        self.assertEqual(df["EP"].iloc[1], 0.)
        
        
if __name__ == "__main__":
    
    unittest.main()
        