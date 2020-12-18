# 输入某年某月某日，判断这一天是这一年的第几天？

year = int(input("year:")) # 输入年
month = int(input("month:")) # 输入月
day = int(input("day:")) # 输入日
months = (0, 31, 59, 120, 151, 181, 212, 243, 273, 304, 334) # 共12个月需加的天数分别是1月需加0天，2月需加31天 3月需加59天...
if 0 < month <= 12:
    sum = months[month - 1]
    sum += day
    if(year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) and (month > 2): # 闰年判断标准 1.能整除4且不能整除100   2、能整除400
        sum += 1
    print("%s年%s月%s日" % (year, month, day), "是%s年的第%d天" % (year, sum))

else:
    print("您输入的日期错误")

