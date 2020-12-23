# 1+11+111+1111+11111+...的和
def fun(n):
    sum = 0
    x = 0
    for i in range(1, n):
        x = x*10 +1
        sum += x
    print(sum)

fun(6)