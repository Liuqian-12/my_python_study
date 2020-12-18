# 输入三个整数x,y,z，请把这三个数由小到大输出

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
listNum = []
listNum.append(x)  # append 方法添加列表项
listNum.append(y)
listNum.append(z)
listNum.sort()
for i in listNum:
    print(i)

