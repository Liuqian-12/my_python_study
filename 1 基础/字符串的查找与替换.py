hello_str = "hello world"
# 判断是否以指定字符串开始 
print(hello_str.startswith("hello"))
# 判断是否以指定字符串结束 
print(hello_str.endswith("world"))
# 查找指定字符串 (find:如果指定的字符串不在，会返回-1；index：会报错)
print(hello_str.find("llo"))
print(hello_str.find("abc"))

'''
print(hello_str.index("llo"))
print(hello_str.index("abc"))

'''
# 替换字符串 (replace方法执行完成后，会返回一个新的字符串， 不会修改原有字符串的内容)
print(hello_str.replace("hello", "python"))

print(hello_str)