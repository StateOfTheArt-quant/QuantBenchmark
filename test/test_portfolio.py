#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import pandas as pd

from quant_benchmark.strategy.portfolio import long_short_portfolio

class PortfolioTest(unittest.TestCase):
    
    def test_portfolio(self):
        estimate_return = pd.Series([0.05, 0.03, -0.02, 0.01, -0.075], index=["000001.XSHE","000002.XSHE","000004.XSHE","000008.XSHE","000012.XSHE"])
        long, short = long_short_portfolio(estimate_return, long_percent=0.1, short_percent=0.4)
        self.assertEqual(long, ["000001.XSHE"])
        self.assertEqual(short, ["000004.XSHE", "000012.XSHE"])
        
if __name__ == "__main__":
    
    unittest.main()