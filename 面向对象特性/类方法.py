class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0
    
    # 类方法
    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name

        # 让类属性的值 +1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("lang头")
Tool.show_tool_count()

        