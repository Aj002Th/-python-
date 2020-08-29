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
# ���⣺����һ��֮���ƻ������б���


myRev = MyRev("FishC")
for i in myRev:
    print(i, end='')


class MyRev:  # �����������ţ�������Ϊ�����ƻ����б���
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
