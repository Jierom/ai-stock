import tushare as ts
import datetime
import json
from account import MyAccount
from strategy.delta_strategy import DeltaStrategy

if __name__ == '__main__':
    # 获取数据源
    df = ts.get_hist_data('000876', '2020-10-03', '2021-02-03')
    df = df.iloc[::-1]

    # 初始化账号    
    my_account = MyAccount(stock=3, cost=df.ix[0]['open'], money=50000)

    # 处理每日
    for row in df.iterrows():
        date = row[0]
        data = row[1]
        strategy = DeltaStrategy()
        strategy.daily_run(my_account, date, data)

    my_account.display_init()
    my_account.display_total(df.ix[-1]['close'])
