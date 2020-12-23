import json

raw_json = {
    "key1": 1,
    "key2": "1",
    "key3": [1, "1"],
    "key4": {
        "key5": 1
    }
}

# json.dumps()将一个python数据结构转换为json
json_str = json.dumps(raw_json)
print(repr(json_str))