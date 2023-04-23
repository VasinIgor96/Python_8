filename = "hello.txt"  

search_string = input("Введіть рядок для пошуку: ")


with open(filename, "r") as file:

    content = file.read()
    if search_string in content:
        print("Рядок знайдено: ", search_string)
    else:
        print("Рядок не знайдено: ", search_string)