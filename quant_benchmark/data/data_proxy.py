from quant_benchmark.interface import AbstractDataSource
from quant_benchmark.data.trading_dates_mixin import TradingDatesMixin
from quant_benchmark.data.base_data_source.default_data_source import DefaultDataSource


class DataProxy(TradingDatesMixin):
    
    _instance = None
    def __new__(cls, *args, **kwars):
        if cls._instance is None:
            cls._instance = super(DataProxy, cls).__new__(cls)
        return cls._instance
            
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            data_source = DefaultDataSource()
            return DataProxy(data_source)
        return cls._instance
    
    def __init__(self, data_source):
        if not isinstance(data_source, AbstractDataSource):
            raise RuntimeError("data_source must inherit from AbstracDataSource interface")
        self._data_source = data_source
        TradingDatesMixin.__init__(self, data_source.get_trading_calendar())
    
    def history_bars(self, order_book_ids, bar_count, dt, fields=None, frequency='1d',skip_suspended=True, include_now=True, adjust_type="pre", adjust_orig=None):
        return self._data_source.history_bars(order_book_ids=order_book_ids, bar_count=bar_count, dt=dt, fields=fields, frequency=frequency,skip_suspended=skip_suspended, include_now=include_now, adjust_type=adjust_type, adjust_orig=adjust_orig)
    
    def history_fundamentals(self, order_book_ids, bar_count, dt, fields=None, frequency='1d',skip_suspended=True, include_now=True, adjust_type="pre", adjust_orig=None):
        return self._data_source.history_fundamentals(order_book_ids=order_book_ids, bar_count=bar_count, dt=dt, fields=fields, frequency=frequency,skip_suspended=skip_suspended, include_now=include_now, adjust_type=adjust_type, adjust_orig=adjust_orig)
    
    def history_tradings(self, order_book_ids, bar_count, dt, fields=None, frequency='1d',skip_suspended=True, include_now=True, adjust_type="pre", adjust_orig=None):
        return self._data_source.history_tradings(order_book_ids=order_book_ids, bar_count=bar_count, dt=dt, fields=fields, frequency=frequency,skip_suspended=skip_suspended, include_now=include_now, adjust_type=adjust_type, adjust_orig=adjust_orig)
