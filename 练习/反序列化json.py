import json

# json.loads()将一个json编码的字符串转换回一个python数据结构
json_str = '{"key3": [1, "1"], "key2": "1", "key1": 1, "key4": {"key5": 1}}'
raw_json = json.loads(json_str)
print(repr(raw_json))