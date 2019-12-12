# QuantBenchmark
quant benchmark in research and production environment

## Cross-sectional regression benchmark

* date_range： 2015-01-05 ： 2019-11-28
* frequency： 1d

### average factor return

| BP          | Beta      | Momentum  | NonLinearSize | Size        | Earningyield | Leverage    | Liquidity   | ResidualVolatility |
|-------------|-----------|-----------|---------------|-------------|--------------|-------------|-------------|--------------------|
| -0.000149   | 0.000269  | 0.000009  | -0.000139     | -0.000356   | 0.000086     | -0.000109   |   -0.000445 |   -0.000113        |
![](https://github.com/StateOfTheArt-quant/QuantBenchmark/assets/images/lr_factor_returns.png)


### r2 score describe
|              | mean       | 25%      | 50%       | 75%       |
|--------------|------------|----------|-----------|-----------|
| relative_r2  | 0.078972   | 0.030036 | 0.053048  | 0.099254  |
| total_r2     | 0.277296   | 0.08425  | 0.194767  | 0.424896  |

## Fama macbeth regression benchmark
### r2 score describe(out of sample)
* rolling window: 5d

|              | mean       | 25%      | 50%       | 75%       |
|--------------|------------|----------|-----------|-----------|
| relative_r2  | -0.839039  |-0.574082 | -0.176542 | -0.046358 |
| total_r2     | -0.012423  |-0.024279 | -0.005865 | 0.006163  |