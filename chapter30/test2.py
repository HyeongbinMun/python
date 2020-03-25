def personal_info(name, age, address):
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)

def fun(**kwargs):
    for k, v in kwargs.items():
        print('{0} : {1}'.format(k, v))

personal_info(name='dk', address='dddddd', age=30)      #키워드 인수(순서 상관없음)
x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}    #key = 문자열
personal_info(**x)      #딕셔너리 언패킹
fun(**x)