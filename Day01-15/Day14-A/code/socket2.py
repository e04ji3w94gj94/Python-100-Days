"""
套接字 - 基於TCP協議創建時間客戶端

Version: 0.1
Author: 骆昊
Date: 2018-03-22
"""

from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 6789))
while True:
    # 3.從服務器接收數據
    data = client.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))
client.close()
