from functools import reduce
def f(x, y):
    return x+y

a = [1, 2, 3, 4,5]
print(reduce(f, a))