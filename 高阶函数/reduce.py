"""
利用reduce累加，((((1+2)+3)+4)+5)
"""
from functools import reduce

print(reduce(lambda a, b: a+b, range(1, 6)))

print(reduce(lambda a, b: a*b, range(1, 6)))

