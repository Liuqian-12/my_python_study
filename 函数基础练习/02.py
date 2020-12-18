# 写函数，专门计算图形的面积

# 其中嵌套函数，计算圆的面积，正方形的面积和长方形的面积
# 调用函数area(‘圆形’,圆半径) 返回圆的面积
# 调用函数area(‘正方形’,边长) 返回正方形的面积
# 调用函数area(‘长方形’,长，宽) 返回长方形的面积
import math
def circle(*args):
    def yuan_circle(r):
        print(math.pi * r * r)

    def zheng_circle(a):
        print(a*a)

    def chang_circle(a, b):
        print(a*b)


c = circle()
c.yuan_circle(3)
# circle.yuan_circle(3)
# circle.zheng_circle(5)
# circle.chang_circle(3, 4)
