class Stack:
    def __init__(self, start=None):
        if start is None:
            start = []
        self.list = start
        for each in self.list:
            self.push(each)

    def isEmpty(self):
        if self.list:
            return True
        else:
            return False

    def push(self, a):
        self.list.insert(0, a)
        if len(self.list) == 7:
            self.list.pop()

    def pop(self):
        self.list.pop(0)

    def top(self):
        return self.list[0]

    def bottom(self):
        return self.list[-1]