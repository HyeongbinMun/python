x = 10  # 전역 변수
def foo1():
    x = 20  # x는 foo의 지역 변수
    print(x)  # foo의 지역 변수 출력
foo1()
print(x)  # 전역 변수 출력

def foo2():
    global x     # 전역 변수 x를 사용하겠다고 설정
    x = 20  # x는 전역 변수
    print(x)  # 전역 변수 출력
foo2()
print(x)  # 전역 변수 출력