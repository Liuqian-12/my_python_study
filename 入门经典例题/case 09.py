# 题目 暂停一秒输出。

# 程序分析 使用 time 模块的 sleep() 函数。
# Python 编程中使用 time 模块可以让程序休眠，
# 具体方法是time.sleep(秒数)，其中"秒数"以秒为单位，可以是小数，0.1秒则代表休眠100毫秒。 


import time
for i in range(4):
    print(str(int(time.time()))[-2:])
    time.sleep(1)