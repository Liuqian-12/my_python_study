def sum_numbers(num):
    print(num)

    # 递归函数的出口，否则会出现死循环
    if num == 0:
        return num
    sum_numbers(num - 1)

sum_numbers(3)