def min_max(*args):
    the_max = args[0] # 初始化最大值
    the_min = args[0] # 初始化最小值
    for i in args: 
        if i >the_max:
            the_max = i
        elif i<the_min:
            the_min = i

    return {"max": the_max, "min:": the_min}
            

print(min_max(1, 2, 4, 6))

