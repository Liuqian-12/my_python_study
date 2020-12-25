import requests

url = "https://account.cnblogs.com/api/captcha?timestamp=1608789926838&action=SignIn"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

s = requests.session()
r = s.get(url, headers=headers, verify=False)
print(s.cookies)

# 添加登录需要的两个cookie
c = requests.cookies.RequestsCookieJar()
c.set(".CNBlogsCookie", "B71F78924A395AB06F181CDE42EDEA69D2B7C4F6DB52F3953BD645991D375752389F41CA3123119BE803063BA664E1243C6DAEE791CB4FC97F56CDE725B5F157969A26D9AE71A383CAA0C01DC1A46F355338FE7D")
c.set(".Cnblogs.AspNetCore.Cookies", "CfDJ8AHUmC2ZwXVKl7whpe9_lau9QWIBSbHpnF5bEV6dcqKP7sFuCRkR0gCSskCvPwowezxT7TOQoJl0CLpWH4vkyrbdQFRFu9vcy2MgnEslQTVmWOChobec6Rkap5F4_o856Gv8EkUyVpHyOKSx1gtkaR71y1kX8QHgxtGGByvfPMAaKlE7D8w7Cl1rkYwjAClxlnWq6KIpbsR6xZ0TkRJnPDSHtAwUYira7_mUHN7ScUf3tw-X3nA1WUWT41eTL7WZpKjAGpYP5QqhQyAhwYa6bP9j-kQ4rPdKfDAydKivYI-YmVqvBYAmJXNZZQTBaCAd1ZLoL-8kl8-64fKhUP4wYBUT8VStetf8jRX2fQtZiW4ai5x5elEZPWi4aSSInWyQ1ro7-t4HWRAnIUkfj3oGau0uiKGsm3Dau-gyedQ_V0EBL3LOynYunDl12IML6-5bDy8F66_rP-YbNu-_pJh0DaisBBQISeEBjs4jSNdaaI_DxYjyVUyD7thyZPUuGLaHy0yRZWCE02AQvwjzAJ2v-8NGH8uk8hdrY8Euus87X2fU8EQ44mcrC3Sz1SkytNqbwQ")
s.cookies.update(c)
print(s.cookies)