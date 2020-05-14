def A():
    x = 10              # function A 의 지역 변수
    y = 100             # function A 의 지역 변수
    def B():
        x = 20          # function B 의 지역 변수
        def C():
            """nonlocal : 상위의 지역 혹은 전역 변수 호출(계단형 검색)"""
            nonlocal x  # function A 의 지역 변수 호출
            nonlocal y  # function B 의 지역 변수 호출
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()
A()