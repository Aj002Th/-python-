for each in range(5):
    print(each)

it = iter(range(5))
while 1:
    try:
        print(next(it))
    except StopIteration:
        break
