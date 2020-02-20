a = [10, 20, 30, 20]
a.sort()
a.reverse()
print(a)
for index, value in enumerate(a, start=1):
    print(index, value)
for i in range(len(a)):
    print(a[i])
b = list(i for i in range(10))    # 0부터 9까지 숫자를 생성하여 리스트 생성
b = [i for i in range(10)]    # 0부터 9까지 숫자를 생성하여 리스트 생성
print(b)
c = [i for i in range(10) if i % 2 == 0]    # 0~9 숫자 중 2의 배수인 숫자(짝수)로 리스트 생성
print(c)
d = [i * j for j in range(2, 10)
           for i in range(1, 10)]
print(d)
