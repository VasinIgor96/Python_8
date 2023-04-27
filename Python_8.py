with open('hello.txt', 'r') as file:
    def tail(filename, n):
        if n <= 0:
            print("Некоректна кількість рядків для виведення")
            return

        with open(filename, 'r') as file:
            lines = file.readlines()
            if len(lines) < 3:
                print("Весь файл:")
                print(''.join(lines))
            else:
                print(f"Останні {3} рядки: ")
                for line in lines[-3:]:
                    print(line, end='')
                    print('')
    tail("hello.txt", 3)
