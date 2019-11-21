#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import jqdatasdk

from xqdata.base_data_source.default_data_source import DefaultDataSource
from quant_benchmark.featurizers.feature_creator import create_raw_feature
from quant_benchmark.featurizers.feature_processing import preprocess_raw_feature
from quant_benchmark.model.sklearn_models import skols
from quant_benchmark.model_train.trainer import Trainer
from quant_benchmark.strategy.portfolio import predict_return, long_short_portfolio

###############################################################################
#                               step0 data                                    #
###############################################################################
#input your jqdata username and password
jqdata_username = os.environ["JQDATA_USERNAME"]
jqdata_password = os.environ["JQDATA_PASSWORD"]
jqdatasdk.auth(username=jqdata_username, password=jqdata_password)


order_book_ids = ["000001.XSHE","000002.XSHE","000016.XSHE","000008.XSHE","600000.XSHG","300072.XSHE"]
trading_fields = ["open","high","low","close","volume"]

bar_count = 7
dt = "2019-11-19"
frequency = "1d"

data_source = DefaultDataSource() 
data = data_source.history_bars(order_book_ids=order_book_ids,bar_count=bar_count, frequency=frequency, dt=dt, fields=trading_fields)


###############################################################################
#                            step1 featurizer                                 #
###############################################################################
raw_featurized = create_raw_feature(data)
featurized = preprocess_raw_feature(raw_featurized, lower_bound=0.1, upper_bound=0.9)


###############################################################################
#                              step2 train                                    #
###############################################################################
dt = data.index.levels[1][-1]
exposure_dt = featurized.xs(dt, level="datetime").drop("Label",axis=1)
#
exposure = featurized.reset_index()
exposure = exposure.loc[exposure["datetime"]!=dt]
exposure = exposure.set_index(["order_book_id", "datetime"])

lr_model = skols()
trainer = Trainer(lr_model)
lr_coef, r2_score = trainer.sklearn_trainer(exposure, label_name="Label")
lr_coef = lr_coef.mean()


###############################################################################
#                            step3 portfolio                                  #
###############################################################################
lr_estimate_return = predict_return(exposure=exposure_dt, factor_return=lr_coef)
lr_long, lr_short= long_short_portfolio(lr_estimate_return, long_percent=0.1, short_percent=0.1)
print("lr long portfolio: ", lr_long)
print("lr short portfolio: ", lr_short)


