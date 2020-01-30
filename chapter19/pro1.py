high = int(input())
for i in range(high-1,-1,-1):
    n = 0
    for j in range(high):
        if j >= i:
            print('*', end='')
            n += 1
        else:
            print(' ', end='')
        if j == high-1:
            for a in range(n-1):
                print('*', end='')
    print()