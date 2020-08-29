class Word(str):
    def __init__(self, ok):
        if " " in ok:
            self.long = len(self.split(' ')[0])
        else:
            self.long = len(self)
        super().__init__()

    def __lt__(self, other):
        return bool(self.long < other.long)

    def __le__(self, other):
        return bool(self.long <= other.long)

    def __eq__(self, other):
        return bool(self.long == other.long)

    def __ne__(self, other):
        return bool(self.long != other.long)

    def __gt__(self, other):
        return bool(self.long > other.long)

    def __ge__(self, other):
        return bool(self.long >= other.long)


if Word("abcde") > Word("abc blue"):
    print(123456)



class Word1(str):
'''存储单词的类，定义比较单词的几种方法'''   # 去第一个空格前的单词为参数

    def __new__(cls, word):
        # 注意我们必须要用到 __new__ 方法，因为 str 是不可变类型
        # 所以我们必须在创建的时候将它初始化
        if ' ' in word:
            print "Value contains spaces. Truncating to first space."
            word = word[:word.index(' ')] #单词是第一个空格之前的所有字符
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)
