"""
用while循環實現1~100之間的偶數求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

sum = 0
num = 2
while num <= 100:
    sum += num
    num += 2
print(sum)
