import requests
payload = {"alyssa": "hello", "python": "hello python"}

r = requests.post("http://httpbin.org/post", params=payload)
print(r.text)