class Nlist:
    def __init__(self, *n):
        self.list = [*n]
        self.count = {}
        for each in range(len(self.list)):
            self.count[each] = 0

    def __len__(self):
        return len(self.list)

    def __getitem__(self, item):
        self.count[item] += 1
        return self.list[item]


c1 = Nlist(1, 3, 5, 7, 9)
c2 = Nlist(2, 4, 6, 8, 10)
print(c1[1])
print(c2[1])
print(c1[1] + c2[0])
print(c1.count)
print(c2.count)