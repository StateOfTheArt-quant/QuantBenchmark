#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import torch
from quant_benchmark.featurizers.default_featurizer import DefaultFeaturizer

def create_raw_feature(raw_data: pd.DataFrame) -> pd.DataFrame :  

    use_cuda = torch.cuda.is_available()
    device = torch.device('cuda' if use_cuda else 'cpu')
    
    open_ts = torch.tensor(raw_data["open"].unstack(0).values, dtype=torch.float32, device=device)    
    high_ts = torch.tensor(raw_data["high"].unstack(0).values, dtype=torch.float32, device=device)
    low_ts = torch.tensor(raw_data["low"].unstack(0).values, dtype=torch.float32, device=device)
    close_ts = torch.tensor(raw_data["close"].unstack(0).values, dtype=torch.float32, device=device)
    volume_ts = torch.tensor(raw_data["volume"].unstack(0).values, dtype=torch.float32, device=device)
    
    featurizer = DefaultFeaturizer()
    feature_list, feature_name_list = featurizer.forward(open_ts, high_ts, low_ts, close_ts, volume_ts)
    
    data_container = {}
    for i, feature in enumerate(feature_list):
        raw_feature_df = pd.DataFrame(feature.cpu().numpy(), index=raw_data.index.levels[1], columns=raw_data.index.levels[0])
        data_container[feature_name_list[i]] = raw_feature_df
        
    featured_df = pd.concat(data_container)
    featured_df = featured_df.stack(0).unstack(0).swaplevel(0,1).sort_index(level=0)
    return featured_df.rename_axis(index=["order_book_id", "datetime"])