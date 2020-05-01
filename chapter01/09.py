import random
doc = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
doc = doc.split(' ')
doc_list = []
for word in doc:
    if len(word) >= 4:
        w = word[1:-1]
        w_list = [w[i] for i in range(len(w))]
        random.shuffle(w_list)
        tmp = ''
        for j in w_list:
            tmp += j
        processed_word = word[0] + tmp + word[-1]
        doc_list.append(processed_word)
        
    else:
        doc_list.append(word)

print(doc_list)
