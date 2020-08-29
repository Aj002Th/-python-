y = [1, 3, 5, 7, 9]
z = [2, 4, 6, 8, 10]
i = list(map(lambda x : list(x),zip(y,z)))
print(i)

list(map(lambda x, y : [x, y], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]