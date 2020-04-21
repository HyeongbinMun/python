def plus_ten(x):
    return x + 10
print(plus_ten(1))

plus_ten1 = lambda x: x + 10
print(plus_ten1(1))
print((lambda x: x + 10)(1))

print(list(map(lambda x: x + 10, [1, 2, 3])))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))