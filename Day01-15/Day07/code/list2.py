"""
列表常用操作
- 列表连接
- 获取长度
- 遍历列表
- 列表切片
- 列表排序
- 列表反转
- 查找元素

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 循環遍歷列表元素
    for fruit in fruits:
        print(fruit.title(), end=' ')
    print()
    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)
    # fruit3 = fruits  # 沒有復制列表只創建了新的引用
    # 可以通過完整切片操作來複製列表
    fruits3 = fruits[:]
    print(fruits3)
    fruits4 = fruits[-3:-1]
    print(fruits4)
    # 可以通過反向切片操作來獲得倒轉後的列表的拷貝 
    fruits5 = fruits[::-1]
    print(fruits5)


if __name__ == '__main__':
    main()
