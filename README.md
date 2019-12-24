# QuantBenchmark
quant benchmark in research and production environment

## Cross-sectional regression benchmark

* date_range： 20150105-20191128
* frequency： 1d

### average factor return

|                  | BP          | Beta      | Momentum   | NonLinearSize | Size        | Earningyield | Leverage    | Liquidity   | ResidualVolatility |
|------------------|-------------|-----------|------------|---------------|-------------|--------------|-------------|-------------|--------------------|
|all stocks        | -0.000149   | 0.000269  | 0.000009   | -0.000139     | -0.000356   | 0.000086     | -0.000109   |   -0.000445 |   -0.000113        |
|size top70% stocks| -0.000127   | 0.000218  | -0.000023  | -0.000147     | -0.000147   | 0.000099     | -0.000097   |   -0.000388 |   -0.000047        |

* all stocks
![image](https://github.com/yoyo182487329/QuantBenchmark/blob/master/assets/images/lr_factor_returns.png)
* Stocks in the top 70% of the market capitalization
![image](https://github.com/yoyo182487329/QuantBenchmark/blob/master/assets/images/lr_factor_returns_.png)

### r2 score describe

* all stocks

|              | mean       | 25%      | 50%       | 75%       |
|--------------|------------|----------|-----------|-----------|
| relative_r2  | 0.078972   | 0.030036 | 0.053048  | 0.099254  |
| total_r2     | 0.277296   | 0.08425  | 0.194767  | 0.424896  |

* Stocks in the top 70% of the market capitalization

|              | mean       | 25%      | 50%       | 75%       |
|--------------|------------|----------|-----------|-----------|
| relative_r2  | 0.096583   | 0.037077 | 0.068890  | 0.122384  |
| total_r2     | 0.288051   | 0.097129 | 0.210451  | 0.429152  |

## Fama macbeth regression benchmark
### r2 score describe(out of sample)
#### rolling window: 5d

* all stocks

|              | mean       | 25%      | 50%       | 75%       |
|--------------|------------|----------|-----------|-----------|
| relative_r2  | -0.839039  |-0.574082 | -0.176542 | -0.046358 |
| total_r2     | -0.012423  |-0.024279 | -0.005865 | 0.006163  |

* Stocks in the top 70% of the market capitalization

|              | mean       | 25%      | 50%       | 75%       |
|--------------|------------|----------|-----------|-----------|
| relative_r2  | -0.766452  |-0.585701 | -0.190020 | -0.048535 |
| total_r2     | -0.017311  |-0.030420 | -0.009169 | 0.005953  |

#### rolling window: 10d

* all stocks

|              | mean       | 25%      | 50%       | 75%       |
|--------------|------------|----------|-----------|-----------|
| relative_r2  | -0.832098  |-0.562397 | -0.164592 | -0.037761 |
| total_r2     | -0.006273  |-0.014106 | -0.002179 | 0.006928  |

* Stocks in the top 70% of the market capitalization

|              | mean       | 25%      | 50%       | 75%       |
|--------------|------------|----------|-----------|-----------|
| relative_r2  | -0.755753  |-0.570511 | -0.167731 | -0.041683 |
| total_r2     | -0.008515  |-0.019181 | -0.003778 | 0.007509  |

#### rolling window: 20d

* all stocks

|              | mean       | 25%      | 50%       | 75%       |
|--------------|------------|----------|-----------|-----------|
| relative_r2  | -0.825958  |-0.553534 | -0.159396 | -0.035826 |
| total_r2     | -0.003558  |-0.010202 | -0.001158 | 0.006298  |

* Stocks in the top 70% of the market capitalization

|              | mean       | 25%      | 50%       | 75%       |
|--------------|------------|----------|-----------|-----------|
| relative_r2  | -0.747914  |-0.562612 | -0.162677 | -0.036368 |
| total_r2     | -0.004978  |-0.013814 | -0.001941 | 0.007269  |

