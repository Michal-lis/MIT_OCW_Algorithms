import timeit
import random


# function to find  in lists
def find(lis, num):
    if num in lis:
        return lis.index(num)
    else:
        return False


# there is no dedicated function to find a value in Python dict, we convert the keys/values to a list and use list.index[value]

l = [random.randrange(1, 200, 1) for _ in range(10000)]
k = [random.randrange(1, 200, 1) for _ in range(10000)]
v = [random.randrange(1, 200, 1) for _ in range(10000)]
dic = dict(zip(k, v))
# print(l[130])
# print(dic[130])
# print(find(l, 130))
print("List", timeit.timeit('l[130]', globals=globals()))
print("Dict", timeit.timeit('dic[130]', globals=globals()))


l = [random.randrange(1, 200, 1) for _ in range(100000)]
k = [random.randrange(1, 200, 1) for _ in range(100000)]
v = [random.randrange(1, 200, 1) for _ in range(100000)]
dic = dict(zip(k, v))
# print(l[130])
# print(dic[130])
# print(find(l, 130))
print("List", timeit.timeit('l[130]', globals=globals()))
print("Dict", timeit.timeit('dic[130]', globals=globals()))


l = [random.randrange(1, 200, 1) for _ in range(1000000)]
k = [random.randrange(1, 200, 1) for _ in range(1000000)]
v = [random.randrange(1, 200, 1) for _ in range(1000000)]
dic = dict(zip(k, v))
# print(l[130])
# print(dic[130])
# print(find(l, 130))
print("List", timeit.timeit('l[130]', globals=globals()))
print("Dict", timeit.timeit('dic[130]', globals=globals()))