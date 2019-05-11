"""
多個線程共享數據 - 沒有鎖的情況

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

from time import sleep
from threading import Thread


class Account(object):

    def __init__(self):
        self._balance = 0

    def deposit(self, money):
        # 計算存款後的餘額
        new_balance = self._balance + money
        # 模擬受理存款業務需要0.01秒的時間
        sleep(0.01)
        # 修改賬戶餘額
        self._balance = new_balance

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # 創建100個存款的線程向同一個賬戶中存錢
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的線程都執行完畢
    for t in threads:
        t.join()
    print('賬戶餘額為: ￥%d元' % account.balance)

if __name__ == '__main__':
    main()
