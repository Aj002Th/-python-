def myRev(seq):
    index = len(seq) - 1
    while index + 1:
        yield seq[index]
        index -= 1


for i in myRev("FishC"):
    print(i, end='')


def myRev(data):
    # ������ range ���� data �ĵ�������
    # ע�⣬range �Ľ���λ���ǲ�������
    for index in range(len(data)-1, -1, -1):
        yield data[index]