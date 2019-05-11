import re


def main():
    poem = '窗前明月光，疑是地上霜。舉頭望明月，低頭思故鄉。'
    sentence_list = re.split(r'[，。, .]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)  # ['窗前明月光', '疑是地上霜', '舉頭望明月', '低頭思故鄉']


if __name__ == '__main__':
    main()