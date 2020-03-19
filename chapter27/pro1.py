with open('words.txt', 'r') as file:
    word = file.read()
    words = list(word.split())
    for i in range(len(words)):
        if 'c' in words[i]:
            print(words[i].strip(',.'))