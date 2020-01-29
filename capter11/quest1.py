x = input().split()
for i in range(5):
    del x[-1]
print(tuple(x))