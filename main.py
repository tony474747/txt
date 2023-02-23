import os

path = './files/'


def readfile(path: str):
    files_list = os.listdir(path)
    final_text = {}
    for files in files_list:
        if files.rfind('.txt', -4):
            with open(os.path.join(path, files), 'r') as file:
                final_text[files] = file.readlines()

    with open('final_file.txt', 'w') as file:

        for file_name, rows in sorted(final_text.items(), key=lambda x: len(x[-1])):
            file.write(file_name + '\n')
            file.write(str(len(rows)) + '\n')
            if '\n' not in rows[-1]:
                rows[-1] += '\n'
            file.write(''.join(rows))


readfile(path)