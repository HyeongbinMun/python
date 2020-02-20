from pprint import pprint
a = [[10, 20, 30], [30, 40], [50, 60]]
print(a)
pprint(a, indent=4, width=20)
pprint(a, width=20)

for i in range(len(a)):  # 세로 크기
    print(i+1, '행 : ', end='')
    for j in range(len(a[i])):  # 가로 크기
        print(a[i][j], end=' ')
    print()