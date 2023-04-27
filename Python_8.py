

filename = "hello.txt"
search_word = input("Введіть слово для пошуку: ")

with open(filename, "r") as file:
    for line in file:
        if search_word in line:
            print(line)
