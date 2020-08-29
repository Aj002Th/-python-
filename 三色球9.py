print('red    yellow    green')
for red in range(0,4):
    for yellow in range(0,4):
        for green in range(0,7):
            if red + yellow + green ==8:
                print(red,'    ',yellow,'    ',green)
