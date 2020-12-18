def demo(num, num_list):
    
    print("函数内部代码")
    num += num

    # 列表变量使用 + 不会做相加再赋值的操作！ 
    # num_list = num_list + num_list
    # 本质上是调用列表中的 extend 方法
    num_list += num_list
    # num_list.extend(num_list)

    print(num)
    print(num_list)
    print("函数执行完成")

gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)