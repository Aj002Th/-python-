class Celsius:
    def __get__(self, instance, owner):
        return self.value_cel

    def __set__(self, instance, value):
        self.value_cel = value


class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
         instance.cel = (float(value) - 32) / 1.8


class Temperature:
    cel = Celsius()
    fah = Fahrenheit()


t1 = Temperature()
t1.cel = 37
print(t1.fah)
t1.fah = 98
print(t1.cel)
