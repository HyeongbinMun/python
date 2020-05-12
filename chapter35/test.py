class Person:
    bag = []                        # 클래스 속성

    def __init__(self):
        self.bag = []               # 인스턴스 속성
    def put_bag(self, stuff):
        Person.bag.append(stuff)


james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)