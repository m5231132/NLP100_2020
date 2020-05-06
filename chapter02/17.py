with open('popular-names.txt', 'r') as f:
    docx = f.read().split('\n') 
    docx = docx[:-1]
    name_list = []

    for doc in docx:
        word = doc.split(' ')
        name = word[0]
        name_list.append(name)
    name_list = set(name_list)
    name_list = sorted(name_list)
    print(name_list)
    