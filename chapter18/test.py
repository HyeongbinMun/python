for i in range(10000):    # 0부터 9999까지 반복
    print(i)
    if i == 2:    # i가 100일 때
        print('end')
        break       # 반복문을 끝냄. for의 제어흐름을 벗어남

for i in range(10):       # 0부터 99까지 증가하면서 100번 반복
    if i % 2 == 0:         # i를 2로 나누었을 때 나머지가 0면 짝수
        continue           # 아래 코드를 실행하지 않고 건너뜀
    print(i)