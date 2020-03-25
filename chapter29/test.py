def hello():
    print('hello world')

def add(num1, num2):
    """독스트링"""
    print(num1 + num2)

hello()
add(1.3, 2.5)
print(add.__doc__)