"""
使用Process類創建多個進程

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

# 啟動兩個進程，一個輸出Ping，一個輸出Pong，兩個進程輸出的Ping和Pong加起來一共10個

from multiprocessing import Process, Queue
from time import sleep


def sub_task(string, q):
    number = q.get()
    while number:
        print('%d: %s' % (number, string))
        sleep(0.001)
        number = q.get()


def main():
    q = Queue(10)
    for number in range(1, 11):
        q.put(number)
    Process(target=sub_task, args=('Ping', q)).start()
    Process(target=sub_task, args=('Pong', q)).start()


if __name__ == '__main__':
    main()
