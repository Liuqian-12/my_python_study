a = 6
b = 100

# 解法1：使用其他变量
#  c = a
#  a = b
#  b = c

# 解法2：不使用其他变量
# a = a + b
# b = a - b
# a = a - b

# 解法3：python专用（利用元组）
# a, b = (b, a)
# 等号右边是元组
a, b = b, a

print(a)
print(b)
