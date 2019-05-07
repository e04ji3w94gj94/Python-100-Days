"""
用for循環實現1~100之間的偶數求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

sum = 0
# 可以產生一個2到100的偶數序列，其中的2是步長，即數值序列的增量。
for x in range(2, 101, 2):
    sum += x
print(sum)
