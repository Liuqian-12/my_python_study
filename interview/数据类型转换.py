# 在进行转换之间先研究下python中list和array（np.array）的不同：
# 1、list是python中内置的数据类型，其中的数据的类型可以不相同，如java中List也可以不用相同的数据，但是为了格式的统一，就要用到泛型或者ArrayList。array中的数据类型必须是一样的。
# 2、list中保存的数据的存放地址，而不是数据，会增加内存的占用，所以存放数据还是尽量使用array。
# 3、list中有append的方法，可以进行追加，而array没有追加的方法，只能通过np.append来实现追加。
# 4、在print的时候，打印的结果不同。list元素之间有","分割，而array之间是空格。
print('-----------------list和array-------------------')
import numpy as np
list1 = [1, 2, 3, 4]
arr1 = np.array(list1)
print(list1)
print(arr1)

print('-----------------list转换为str-------------------')
# 当list中存放的数据是字符串时，一般是通过str中的join函数进行转换：
list2 = ['a','b','c','d']
str1 = ''.join(list2)
str2 = ' '.join(list2)
str3 = '.'.join(list2)
print(str1)
print(str2)
print(str3)
# 但是当list中存放的数据是整型数据或者数字的话，需要先将数据转换为字符串再进行转换：
list3 = [1, 2, 3, 4, 5]
str_1 = ''.join([str(x) for x in list3])
str_2 = ' '.join([str(x) for x in list3])
str_3 = '.'.join([str(x) for x in list3])
print(str_1)
print(str_2)
print(str_3)

print('-----------------array转换为str-------------------')
# 将array转换为str和list转换时是一样的，join()函数中的参数是一个iterator，所以array或者list都可以。
arr2 = np.array(list2)
str4 = ''.join(arr2)
print(str4)

print('-----------------str转换为list-------------------')
str11 = 'abcde'
str22 = 'a b c d   e'
str33 = 'a, b, c, d, e'
result1 = list(str11)
result2 = str22.split()
result3 = str33.split(', ')
print(result1)
print(result2)
print(result3)
