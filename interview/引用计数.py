import sys
class p1(dict):
    def __del__(self):
        print("删除1")

class p2(dict):
    def __del__(self):
        print("删除2")

a = p1()
b = p2()
a["aa"] = b
b["aa"] = a
print("OK")




   