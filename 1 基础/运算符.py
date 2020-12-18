'''
# + extend append
a_tuple = (1, 2)
b_tuple = (3, 4)
print(a_tuple + b_tuple)

a_list = [1, 2]
b_list = [3, 4]
print(a_list + b_list)

t_list = [1, 2]
t_list.extend([3, 4])
print(t_list)

t_list = [1, 2]
t_list.append(3)
print(t_list)

t_list = [1, 2]
t_list.append([3, 4])
print(t_list)

'''

# 成员运算符
print("a" in "abcde")
print("a" not in "abcde")
print("1" in "[0, 1, 2]")
print("1" not in "[0, 1, 2]")
print("name" in {"name": "xiaoming"})
print("xiaoming" in {"name": "xiaoming"})