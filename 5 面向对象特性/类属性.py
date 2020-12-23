class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0
    def __init__(self, name):
        self.name = name

        # 让类属性的值 +1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("刀")
tool2 = Tool("剑")
tool3 = Tool("钉")

# 输出工具对象的总数 类名.类属性
# print(Tool.count)

# 不推荐对象.类属性
tool3.count = 99
print("工具对象总数 %d" % tool3.count)

print("---> %d" % Tool.count)

        