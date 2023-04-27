with open('hello.txt', 'r') as file:
    for line in file:
        for word in line.split():
            if word.isdigit():
                print(word)