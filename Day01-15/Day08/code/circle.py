"""
練習
修一個游泳池半徑（以米為單位）在程式運行時輸入游泳池外修一條3米寬的通道
通道的外側修一圈圍牆
已知通道的造價為每平米25元
圍牆的造價為每米32.5元
輸出圍牆和通道的總造價分別是多少錢（精確到小數點後2位）

Version: 0.1
Author: 駱昊
Date: 2018-03-08
"""

import math


class Circle(object):

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius if radius > 0 else 0

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    @property
    def area(self):
        return math.pi * self._radius * self._radius


if __name__ == '__main__':  
    radius = float(input('請輸入游泳池的半徑: '))
    small = Circle(radius)
    big = Circle(radius + 3)
    print('圍牆的造價為: ￥%.1f元' % (big.perimeter * 32.5))
    print('通道的造價為: ￥%.1f元' % ((big.area - small.area) * 25))
