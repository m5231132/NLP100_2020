import sys

def save_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)

n = sys.argv[1]
f = open('popular-names.txt', 'r')
docx = f.readlines()

output_size = len(docx) // int(n)

for i in range(int(n)):
    offset = i * output_size
    text = docx[offset : offset + output_size]
    save_file(str(i), ''.join(text))    