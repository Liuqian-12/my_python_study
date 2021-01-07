# 格式化字符输出
# 定义字符串变量 name，输出 我的名字叫小明，请多多关照！
name = "xiaoming"
print("我的名字叫 %s，请多多关照！" % name) # %s 表示字符串

# 定义整数变量 student_no，输出 我的学号是000001
student_no = 100
print("我的学号是 %06d" % student_no)  # %d 表示十进制整数 %06d 表示占位符

# 
price = 8.5
weight = 7.5
money = price * weight
print("苹果的单价 %.2f 元/斤，购买了 %.3f 斤，需要支付 %.4f 元" % (price, weight, money))  # %f 浮点数

#
scale = 0.25
print("数据比例是 %.2f%%" % (scale * 100))  # %% 输出%