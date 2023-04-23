
filename = "hello.txt"

with open (filename, "r") as file:
    content = file.read()
    words = content.split()
    num_words = len(words)
    print("Кількість слів в файлі:", num_words)
