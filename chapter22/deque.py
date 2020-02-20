from collections import deque    # collections 모듈에서 deque를 가져옴
a = deque([10, 20, 30])
print(a)
deque([10, 20, 30])
a.append(500)    # 덱의 오른쪽에 500 추가
a.appendleft(100)    # 덱의 왼쪽에 100 추가
print(a)
deque([10, 20, 30, 500])
a.popleft()     # 덱의 왼쪽 요소 하나 삭제 -> 10
a.pop()     # 덱의 오른쪽 요소 하나 삭제 -> 500
print(a)
deque([20, 30, 500])