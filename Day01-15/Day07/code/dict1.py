"""
定義和使用字典

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    # 通過鍵可以獲取字典中對應的值
    print(scores['骆昊'])
    print(scores['狄仁杰'])
    # 對字典進行遍歷(遍歷的其實是鍵再通過鍵取對應的值)
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    # 更新字典中的元素
    scores['白元芳'] = 65
    scores['諸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    # get方法也是通過鍵獲取對應的值但是可以設置默認值
    print(scores.get('武则天', 60))
    # 删除字典中的元素
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('骆昊', 100))
    # 清空字典
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()
