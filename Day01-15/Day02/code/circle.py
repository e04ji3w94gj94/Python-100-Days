"""
輸入半徑計算圓的週長和面積

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

import math

radius = float(input('請輸入圓的半徑: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('週長: %.2f' % perimeter)
print('面積: %.2f' % area)
