price = list(map(int, input().split(';')))
price.sort(reverse=True)
for i in range(len(price)):
    print('%9s' % format(price[i], ','))