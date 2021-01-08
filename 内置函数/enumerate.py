list1 = [2, 4, 1, 5, 5]
for index, item in enumerate(list1):   # index表示索引， item表示元素
    print(index, item)

li = ["baby", "honey"]
for item in enumerate(li):
    print(item)

for item in enumerate(li, 12):
    print(item)

for item in enumerate(li, 13):
    print(item[0], item[1])

