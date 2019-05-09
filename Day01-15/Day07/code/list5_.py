def main():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函數返回列表排序後的拷貝不會修改傳入的列表
    # 函數的設計就應該像sorted函數一樣盡可能不產生副作用
    list3 = sorted(list1, reverse=True)
    # 通過key關鍵字參數指定根據字符串長度進行排序而不是默認的字母表順序
    list4 = sorted(list1, key=len)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    # 給列表對象發出排序消息直接在列表對像上進行排序
    list1.sort(reverse=True)
    print(list1)


if __name__ == '__main__':
    main()