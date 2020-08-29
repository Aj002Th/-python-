def myRev(seq):
    index = len(seq) - 1
    while index + 1:
        yield seq[index]
        index -= 1


for i in myRev("FishC"):
    print(i, end='')


def myRev(data):
    # 这里用 range 生成 data 的倒序索引
    # 注意，range 的结束位置是不包含的
    for index in range(len(data)-1, -1, -1):
        yield data[index]