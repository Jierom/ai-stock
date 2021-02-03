#-*- coding: utf-8 -*-

"""
name: 
descripion:
    如果到达当天开盘价的 +3% 则卖出
    如果到达当天开盘价的 -3% 则买入
"""

class DeltaStrategy(object):

    """
    策略参数:
        - st_rate: 盈亏到达率（默认 3%）
        - st_stock: 交易手数（默认 1手）
    """
    def __init__(self, st_rate=0.03, st_stock=1):
        self.st_rate = st_rate
        self.st_stock = st_stock

    def daily_run(self, account, date, data):
        open_price = data['open']

        in_price = data['open'] * (1 + self.st_rate)
        out_price = data['open'] * (1 - self.st_rate)

        # 触发买入
        if data['high'] >= in_price:
            # 现金不足跳过
            if account.money < in_price * self.st_stock * 100:
                pass
            else:
                account.money -= in_price * self.st_stock * 100
                account.stock += self.st_stock
                account.money -= in_price * self.st_stock * 100 * 0.00025  # 手续费
                # print("+++++ {} 以 {} 买入".format(date, in_price))
                # account.display_total(data['close'])

        # 触发卖出
        if data['low'] <= out_price:
            # 股数不足跳过
            if account.stock < self.st_stock:
                pass
            else:
                account.money += out_price * self.st_stock * 100
                account.stock -= self.st_stock
                account.money -= out_price * self.st_stock * 100 * 0.001    # 印花税
                account.money -= out_price * self.st_stock * 100 * 0.00025  # 手续费
                # print("----- {} 以 {} 卖出".format(date, out_price))
                # account.display_total(data['close'])

