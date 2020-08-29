class CountList:  # 如果继承列表会更加方便
    def initialize(self):
        self.count = {}
        for i in range(len(self.values)):
            self.count[i] = self.count_list[i]

    def __init__(self, *args):
        self.values = [x for x in args]
        self.count_list = []
        for x in range(len(self.values)):
            self.count_list.append(0)
        self.initialize()

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count_list[key] += 1
        self.initialize()
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value
        self.count_list[key] = 0
        self.count[key] = 0

    def __delitem__(self, key):
        del self.values[key]
        del self.count_list[key]
        del self.count
        self.initialize()

    def counter(self, key):
        print(self.count_list[key])

    def append(self, value):
        self.values.append(value)
        self.count_list[len(self.values)] = 0
        self.initialize()

    def pop(self, num=-1):
        out = self.values.pop(num)
        del self.count_list[num]
        self.initialize()
        return out

    def remove(self, name):  # remove删除首次出现name的元素！！血惨
        start = 0
        list1 = []
        try:
            while start != -1:
                pos = self.values.index(name, start)
                list1.append(pos)
                start = pos + 1
        except:
            pass

        self.values.remove(name)
        for each in list1:
            del self.count_list[each]
        self.initialize()

    def insert(self, pos, name):
        self.values.insert(pos, name)
        self.count_list.insert(pos, 0)
        self.initialize()

    def clear(self):
        del self.values
        del self.count_list
        del self.count
        self.count = {}

    def reverse(self):
        self.values.reverse()
        self.count_list.reverse()
        self.initialize()
        return self.values


c1 = CountList(1, 3, 5, 7, 9)
c2 = CountList(2, 4, 6, 8, 10)
print(c1[1])
print(c2[1])
print(c1[1] + c2[0])
print(c1.count)
print(c1.count_list)
print(c2.count)
print(c2.count_list)

print(c1.reverse())
print(c1.count_list)

c1.remove(3)
print(c1.values)

print(c1.count)
c2.clear()
print(c2.count)
print(c1.counter(2))


class CountList(list):  # 高手就是会偷懒
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self, key):
        self.count[key] += 1
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self, key):
        return self.count[key]

    def append(self, value):
        self.count.append(0)
        super().append(value)

    def pop(self, key=-1):
        del self.count[key]
        return super().pop(key)

    def remove(self, value):
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key, value)

    def clear(self):
        self.count.clear()
        super().clear()

    def reverse(self):
        self.count.reverse()
        super().reverse()
