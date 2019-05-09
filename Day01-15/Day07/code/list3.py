"""
生成列表
- 用range創建數字列表
- 生成表達式
- 生成器

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""
import sys

# 生成Fibonacci(在一串數字中，每一項是前兩項的和)序列的生成器
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    # 用range創建數值列表列表
    list1 = list(range(1, 11))
    print(list1)
    # 生成表達式 
    list2 = [x * x for x in range(1, 11)]
    print(list2)
    list3 = [m + n for m in 'ABCDEFG' for n in '12345']
    print(list3)
    print(len(list3))

    # 用這種語法創建列表之後元素已經準備就緒所以需要耗費較多的內存空間
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f)) # 查看對象佔用內存的字節數
    print(f)
    # 請注意下面的代碼創建的不是一個列表而是一個生成器對象
    # 通過生成器可以獲取到數據但它不佔用額外的空間存儲數據
    # 每次需要數據的時候就通過內部的運算得到數據（需要花費額外的時間）
    gen = (m + n for m in 'ABCDEFG' for n in '12345')
    print(gen)
    for elem in gen:
        print(elem, end=' ')
    print()
    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))  # 相比生成式生成器不佔用存儲數據的空間
    print(f)
    gen = fib(20)
    print(gen)
    for elem in gen:
        print(elem, end=' ')
    print()


if __name__ == '__main__':
    main()
