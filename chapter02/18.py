with open('popular-names.txt', 'r') as f:
    docx = f.read().split('\n') 
    docx = docx[:-1]
    num_list = []

    for doc in docx:
        word = doc.split(' ')
        num = int(word[2])
        num_list.append(num)
    num_list = sorted(num_list)
    print(num_list)