from functools import reduce

def multiples(num):
    list1 = []
    for i in range(1, num):
        if (i % 3 == 0 or i % 5 == 0):
            list1.append(i)
    res = reduce((lambda x, y : x + y), list1)
    return res

print(multiples(10))