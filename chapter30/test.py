def print_number(a, b, c):
    print(a)
    print(b)
    print(c)

num = [1, 2, 3]
print_number(*num)      #list num을 언패킹(*)

def print_number(*args):    #매개변수를 가변변수로 변경
    for age in args:
        print(age)

num = [1, 2, 3]
print_number(*num)      #list num을 언패킹(*)
