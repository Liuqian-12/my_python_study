xiaoming_dict = {"name": "小明",
                 "age": 18}
                
# 统计键值对数量
print(len(xiaoming_dict))

# 合并字典（注意：如果被合并的字典中包含已存在的键值对， 会覆盖原有的键值对）
temp_dict = {"height": 1.75, 
             "age": 20}
xiaoming_dict.update(temp_dict)

# 清空字典
xiaoming_dict.clear()

print(xiaoming_dict)