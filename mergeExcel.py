import os
import pandas as pd
import time

t1 = time.time()
l = []
n = 0
for file in os.walk('C:\\Users\\facke\\Downloads'):
    for table in file[2]:
        path = file[0] + '/' + table
        data = pd.read_csv(path, header=0, encoding='utf-8', engine='python')
        n = n+1
        l.append(data)
        print('第' + str(n) + '个表格已提取')
data_result = pd.concat(l)
data_result.to_csv('C:\\Users\\facke\\Downloads\\merge.csv', index=0)
t2 = time.time()
t = t2 - t1
t = round(t, 2)
print('用时' + str(t) + '秒')
print('完成')
