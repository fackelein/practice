import tushare as ts

# x52ErW.Ltj9:fhN
# pro = ts.pro_api('8e93501797577e39fcddd6aeb68121edc98066a2d9e3b87fa7cbedf8') #old token
pro = ts.pro_api('535a5b1963f7377d468bc374af5e254b93532d595a6c2a96a8ce0bc1') # token of mobile num
#df = pro.daily(ts_code='002352.SZ', start_date='20211230', end_date='20220114')
# dt = pro.fina_indicator(ts_code='002352.SZ', start_date='20211201', end_date='20220114')
ipo_list = pro.new_share(start_date='20211201', end_date='20220114')
ipo_list.to_csv('ipo.csv')
#print(df.close)


