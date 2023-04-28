while True:
    with open('hello.txt', 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            print(f"{i}: {line.strip()}")
        line_number_to_delete = int(input("Enter line number to delete: "))
        del lines[line_number_to_delete]

    with open('hello.txt', 'w') as f:
        
        f.writelines(lines)