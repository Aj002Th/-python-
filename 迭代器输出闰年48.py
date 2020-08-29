class LeapYear:
    def __init__(self, year=2020):
        self.year = year

    def __iter__(self):
        return self

    def __next__(self):
        while 1:
            self.year -= 1
            if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
                return self.year


leapYears = LeapYear()
for i in leapYears:
    if i >= 2000:
        print(i)
    else:
        break
