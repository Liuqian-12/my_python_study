import requests

url = "http://192.168.112.239:8080/j_acegi_security_check"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

body = {
    "Submit": "Sign in",
    "j_username": "alyssal",
    "j_password": "1212liuqian",
    "from": "/"
}

# 使用session登录
s = requests.session()

# 打印的状态码是200，因为requests库自动处理了重定向请求
r1 = s.post(url, headers=headers, data=body, verify=False)
print(r1.status_code) 

# 设置一个参数禁止重定向：allow_redirects=False
# allow_redirects=True是启动重定向，然后就可以看到status_code是302了
r2 = s.post(url, headers=headers, data=body, allow_redirects=False, verify=False)
print("禁止重定向后的状态码：", r2.status_code)

# 获取Location地址
new_url = r2.headers["Location"]
print("Location:", new_url)
