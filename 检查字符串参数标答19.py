def count(*param):
    length = len(param)
    for i in range(length):
        letters = 0
        space = 0
        digit = 0
        others = 0
        for each in param[i]:
            if each.isalpha():
                letters += 1
            elif each.isdigit():
                digit += 1
            elif each == ' ':
                space += 1
            else:
                others += 1
        print(' %d, %d  %d  %d  %d ' % (i+1, letters, digit, space, others))
            
count('I love fishc.com.', 'I love you, you love me.')
