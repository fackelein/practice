import tushare as ts

pro = ts.pro_api('8e93501797577e39fcddd6aeb68121edc98066a2d9e3b87fa7cbedf8')
df = pro.daily(ts_code='002352.SZ', start_date='20210901', end_date='20210917')
print(df.close)