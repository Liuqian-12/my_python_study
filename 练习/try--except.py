# 用try--except捕获断言异常
res1 = {'code': 1, 'msg': '登陆成功'}
res2 = {'code': 0, 'msg': '登陆失败'}

try:
    assert res1 == res2
except AssertionError as e:
    print("编号A1用例不通过！")
    raise e  # 处理异常后，抛出异常
else:
    print("编号A1用例通过！")

