with open('words.txt', 'r') as file:
    words = file.read().split('\n')
    for word in words:
        word = word.strip('\n')
        if list(word) == list(reversed(word)):
            print(word)