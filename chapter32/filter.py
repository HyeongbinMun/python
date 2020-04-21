def f(x):
    return x > 5 and x < 10
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(f, a)))
