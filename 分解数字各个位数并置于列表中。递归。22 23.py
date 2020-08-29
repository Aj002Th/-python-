def get_digits(n):
    n = int(n)
    if n != 0:
        i = n %10
        n //= 10
        return [i] + get_digits(n)
    else:
        return []
list = list(reversed(get_digits(1234)))
print(list)
