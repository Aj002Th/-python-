class MyRev:
    def __init__(self, seq):
        self.seq = list(seq)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.seq.pop()
        except IndexError:
            raise StopIteration
# 问题：迭代一次之后破坏了序列本身


myRev = MyRev("FishC")
for i in myRev:
    print(i, end='')


class MyRev:  # 利用了索引号，不会因为迭代破坏序列本身
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index = self.index - 1
        return self.data[self.index]
