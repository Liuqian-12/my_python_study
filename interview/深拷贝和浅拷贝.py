import copy

will = ["Will", 28, ["Python", "C#", "JavaScript"]]
# wilber = copy.copy(will)
wilber = copy.deepcopy(will)

print(id(will)) 
print(will) 
print([id(ele) for ele in will]) 
print(id(wilber)) 
print(wilber) 
print([id(ele) for ele in wilber]) 
print('--------------------------------------')

will[0] = "Wilber"
will[2].append("CSS")
print(id(will)) 
print(will) 
print([id(ele) for ele in will]) 
print(id(wilber)) 
print(wilber) 
print([id(ele) for ele in wilber]) 


# 对于非容器类型（如数字、字符串、和其他'原子'类型的对象）没有拷贝这一说
# 也就是说，对于这些类型，"obj is copy.copy(obj)" 、"obj is copy.deepcopy(obj)"
# 如果元祖变量只包含原子类型对象，则不能深拷贝，看下面的例子
print('--------------------------')
will = ("Python", "C#", "JavaScript")
wills = copy.deepcopy(will)
print("1",will)
print("2",wills)
print(will is wills)

will = ("Python", "C#", "JavaScript", [])
print("3", will)
print("4", wills)
print(will is wills)