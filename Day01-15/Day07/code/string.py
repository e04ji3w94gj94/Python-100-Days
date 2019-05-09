def main():
    str1 = 'hello, world!'
    # 通過len函數計算字符串的長度
    print(len(str1)) # 13
    # 獲得字符串首字母大寫的拷貝
    print(str1.capitalize()) # Hello, world!
    # 獲得字符串變大寫後的拷貝
    print(str1.upper()) # HELLO, WORLD!
    # 從字符串中查找子串所在位置
    print(str1.find('or')) # 8
    print(str1.find('shit')) # -1
    # 與find類似但找不到子串時會引發異常
    # print(str1.index('or'))
    # print(str1.index('shit'))
    # 檢查字符串是否以指定的字符串開頭
    print(str1.startswith('He')) # False
    print(str1.startswith('hel')) # True
    # 檢查字符串是否以指定的字符串結尾
    print(str1.endswith('!')) # True
    # 將字符串以指定的寬度居中並在兩側填充指定的字符
    print(str1.center(50, '*'))
    # 將字符串以指定的寬度靠右放置左側填充指定的字符
    print(str1.rjust(50, ' '))
    str2 = 'abc123456'
    # 從字符串中取出指定位置的字符(下標運算)
    print(str2[2]) # c
    # 字符串切片(從指定的開始索引到指定的結束索引)
    print(str2[2:5]) # c12
    print(str2[2:]) # c123456
    print(str2[2::2]) # c246
    print(str2[::2]) # ac246
    print(str2[::-1]) # 654321cba
    print(str2[-3:-1]) # 45
    # 檢查字符串是否由數字構成
    print(str2.isdigit()) # False
    # 檢查字符串是否以字母構成
    print(str2.isalpha()) # False
    # 檢查字符串是否以數字和字母構成
    print(str2.isalnum()) # True
    str3 = ' jackfrued@126.com '
    print(str3)
    # 獲得字符串修剪左右兩側空格的拷貝
    print(str3.strip())


if __name__ == '__main__':
    main()