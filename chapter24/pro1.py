write = input()
words = list(write.split())
count = 0
for i in range(len(words)):
    if words[i].strip(',.') == 'the':
        count += 1
print(count)