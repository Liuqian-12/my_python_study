price_str = input("the price of apples:")
weight_str = input("the weight of apples:")
# 两个字符串之间是不能直接作乘法的，要进行类型转换
# money = price_str * weight_str
price = float(price_str)
weight = float(weight_str)
money = price * weight
print(money)
