def replace_line(filename, old_line, new_line):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            if line.strip() == old_line.strip():
                file.write(new_line + '\n')
            else:
                file.write(line)

replace_line('hello.txt', 'old text', 'new text')
