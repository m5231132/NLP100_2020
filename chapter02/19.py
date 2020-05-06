import collections 
with open('popular-names.txt', 'r') as f:
    docx = f.readlines()
    docx = docx[:-1]
    name_list = []

    for doc in docx:
        word = doc.split(' ')
        name = word[0]
        name_list.append(name)

    c = collections.Counter(name_list)
    print(c)