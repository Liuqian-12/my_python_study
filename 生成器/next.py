list_ = [1, 2, 3, 4, 5]
it = iter(list_)
for i in range(5):
    line = next(it)
    print("第%d 行， %s" %(i, line))