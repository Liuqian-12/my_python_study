# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# import math



for i in range(1, 85):
    if 168 % i == 0:
        j = 168 / i
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(x)


"""

import math
num = 1
while True:
    if math.sqrt(num + 100)-int(math.sqrt(num + 100)) == 0 and math.sqrt(num + 268)-int(math.sqrt(num + 268)) == 0:
        print(num)
        break
    num += 1

"""