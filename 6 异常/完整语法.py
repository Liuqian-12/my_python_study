try:
    num = int(input("输入一个整数："))

    result = 8/num

    print(result)

# except ZeroDivisionError:
#     print("除0错误")

except ValueError:
    print("请输入正确整数")

except Exception as result:
    print("未知错误 %s" % result)

else:
    print("尝试成功")

finally:
    print("无论是否出现错误都会被执行的代码")

print("-" * 50)
