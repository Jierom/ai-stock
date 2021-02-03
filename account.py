#--*-- coding: utf-8 -*-

class MyAccount(object):

    '''
    parameters:
        - stock: 持仓手数
        - money: 初始的现金数
    '''
    def __init__(self, stock, cost, money):
        # 初始化
        self.init_stock = stock
        self.init_cost = cost
        self.init_money = money

        self.stock = stock
        self.money = money

    def display(self):
        print("现有持仓手数:{}, 现有现金:{}".format(self.stock, self.money))

    def display_total(self, cost):
        hold = self.stock * cost * 100
        asset = self.money + hold
        print("[[持仓]] 手数:{}\t成本:{}\t市值:{} \t [[现金]] {} \t [[总资产]] {}".format(self.stock, cost, hold, self.money, asset))

    def display_init(self):
        init_hold = self.init_cost * self.init_stock * 100
        init_asset = self.init_money + init_hold
        print("[[持仓]] 手数:{}\t成本:{}\t市值:{} \t [[现金]] {} \t [[总资产]] {}".format(self.init_stock, self.init_cost, init_hold, self.init_money, init_asset))
