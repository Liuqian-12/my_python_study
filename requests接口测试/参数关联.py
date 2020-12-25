import requests

url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"


s = requests.session()
r1 = s.get(url=url, verify=False)
print(r1.url)
