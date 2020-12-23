for i in range(3):
    str = ''
    for j in range(5-i):
        if i == j or i + j == 4 :
            str += 'v'
        else :
            str += ' '
    print(str)