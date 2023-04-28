
with open('hello.txt', 'r') as file:
    content = file.read()
    lines = content.split('\n')
    unique_lines = set(lines)
    
    if len(lines) == len(unique_lines):
        print('Файл не містить дублікатів! ')
    else:
        print('Файл містить дублікати! ')
