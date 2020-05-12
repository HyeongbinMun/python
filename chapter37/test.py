from math import sqrt, pow

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point2D(x=30, y=20)  # 점1
p2 = Point2D(x=60, y=50)  # 점2

a = p2.x - p1.x  # 선 a의 길이
b = p2.y - p1.y  # 선 b의 길이

c = sqrt(pow(a,2) + pow(b,2))  # (a * a) + (b * b)의 제곱근을 구함
print(c)