'''
在螢幕上顯示跑馬燈文字
'''
import os
import time


def main():
    content = '北京歡迎你為你開天闢地…………'
    while True:
        # 清理螢幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()