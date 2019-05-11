from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('啟動下載進程，進程號[%d].' % getpid())
    print('開始下載%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下載完成! 耗費了%d秒' % (filename, time_to_download))

# 通過Process類創建了進程對象，通過target參數我們傳入一個函數來表示進程啟動後要執行的代碼，
# 後面的args是一個元組，它代表了傳遞給函數的參數。

def main():
    start = time()
    p1 = Process(target=download_task, args=('Python從入門到住院.pdf', ))
    # Process對象的start方法用來啟動進程，而join方法表示等待進程執行結束。
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('總共耗費了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()