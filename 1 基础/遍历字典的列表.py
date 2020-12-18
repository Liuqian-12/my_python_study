student = [
    {"name": "xiaoming"}, 
    {"name": "xiaomei"}
]

find_name = "xiaomei"

for stu_dict in student:

    print(stu_dict)

    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)
        break

else:
    print("抱歉，没有找到")

print("循环结束")