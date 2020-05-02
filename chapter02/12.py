with open('popular-names.txt') as f:
    docx = f.readlines()
    col1 = open('col1.txt','w')
    col2 = open('col2.txt','w')
    for doc in docx:
        word = doc.split(' ')
        col1.write(word[0]+'\n') 
        col2.write(word[1]+'\n') 
col1.close()
col2.close()