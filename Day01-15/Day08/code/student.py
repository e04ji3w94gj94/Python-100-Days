"""
定義和使用學生類

Version: 0.1
Author: 駱昊
Date: 2018-03-08
"""


def _foo():
    print('test')


class Student(object):

    # __init__是一個特殊方法用於在創建對象時進行初始化操作
    # 通過這個方法我們可以為學生對象綁定的名字和年齡兩個屬性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在學習%s.' % (self.name, course_name))

    # PEP 8要求標識符的名字用全小寫多個單詞用下劃線連接
    # 但是很多程式設計師和公司更傾向於使用駝峰命名法（駝峰標識）
    def watch_tv(self):
        if self.age < 18:
            print('%s不能看限制級' % self.name)
        else:
            print('%s任何影片皆可觀看' % self.name)


def main():
    stu1 = Student('骆昊', 38)
    stu1.study('Python程式設計')
    stu1.watch_tv()
    stu2 = Student('王大錘', 15)
    stu2.study('思想品德')
    stu2.watch_tv()


if __name__ == '__main__':
    main()
