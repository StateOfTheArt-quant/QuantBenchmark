#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from quant_benchmark.featurizers.feature_creator import create_raw_feature
from quant_benchmark.featurizers.feature_processing import preprocess_raw_feature
from quant_benchmark.model_train.model_train import training
from quant_benchmark.strategy.portfolio import predict_return, long_short_portfolio

###############################################################################
#                               step0 data                                    #
###############################################################################
bar_count = 20
raw_dict = {}
for i in ["000001.XSHE","000002.XSHE","000016.XSHE","000008.XSHE"]: 
    raw_dict[i] = pd.DataFrame(np.random.randn(bar_count,5), columns=["open","high","low","close","volume"], index=pd.date_range('2019-01-01 00:00:00', periods=bar_count)) 
raw_df = pd.concat(raw_dict)
raw_df.index.names = ["order_book_id", "datetime"]



###############################################################################
#                            step1 featurizer                                 #
###############################################################################
raw_featurized = create_raw_feature(raw_df)
featurized = preprocess_raw_feature(raw_featurized, lower_bound=0.1, upper_bound=0.9)


###############################################################################
#                              step2 train                                    #
###############################################################################
dt = raw_df.index.levels[1][-1]
exposure_dt = featurized.xs(dt, level="datetime").drop("Label",axis=1)
#
exposure = featurized.reset_index()
exposure = exposure.loc[exposure["datetime"]!=dt]
exposure = exposure.set_index(["order_book_id","datetime"])

lr_coef_df, lasso_coef_df, rr_coef_df, en_coef_df = training(exposure, label_name="Label")
lr_coef = lr_coef_df.mean()
lasso_coef = lasso_coef_df.mean()
rr_coef = rr_coef_df.mean()
en_coef = en_coef_df.mean()

###############################################################################
#                            step3 portfolio                                  #
###############################################################################
lr_estimate_return = predict_return(exposure=exposure_dt, factor_return=lr_coef)
lr_long, lr_short= long_short_portfolio(lr_estimate_return, long_percent=0.1, short_percent=0.1)
print("lr long portfolio: ", lr_long)
print("lr short portfolio: ", lr_short)

lasso_estimate_return = predict_return(exposure=exposure_dt, factor_return=lasso_coef)
lasso_long, lasso_short = long_short_portfolio(lasso_estimate_return, long_percent=0.1, short_percent=0.1)
print("lasso long portfolio: ", lr_long)
print("lasso short portfolio: ", lr_short)

rr_estimate_return = predict_return(exposure=exposure_dt, factor_return=rr_coef)
rr_long, rr_short = long_short_portfolio(rr_estimate_return, long_percent=0.1, short_percent=0.1)
print("rr long portfolio: ", lr_long)
print("rr short portfolio: ", lr_short)

en_estimate_return = predict_return(exposure=exposure_dt, factor_return=en_coef)
en_long, en_short = long_short_portfolio(en_estimate_return, long_percent=0.1, short_percent=0.1)
print("en long portfolio: ", lr_long)
print("en short portfolio: ", lr_short)