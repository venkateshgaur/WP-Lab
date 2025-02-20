def reverse_file_content(file1, file2):
    with open(file1, 'r') as f:
        content = f.read()
    reversed_content = content[::-1]
    with open(file2, 'w') as f:
        f.write(reversed_content)

reverse_file_content('file1.txt', 'file2.txt')