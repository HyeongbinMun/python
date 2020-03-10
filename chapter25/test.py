from collections import defaultdict    # collections 모듈에서 defaultdict를 가져옴

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e', 100)
x.update(a=90)
x.update(f=90)
x.pop('a')
print(x)
y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})
y.update(zip([1, 2], ['하나', '둘']))
del y[3]
y.popitem()
y = defaultdict(lambda : '야')
y['z']
print(y.get('z'))