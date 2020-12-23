import requests
import json

url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-1109966897738-ems-UUCAO1608710624586.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

s = requests.session()
r = s.get(url, headers=headers, verify=False)
result = r.json()
data = result["data"]
print(data)
print(data[0])
get_result = data[0]['context']
print(get_result)
if u"已签收" in get_result:
    print("快递单已签收成功")
else:
    print("未签收")

