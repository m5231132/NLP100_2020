def n_gram(txt,n):
    txt_list = txt.split(' ')
    i = 0
    
    ngram = [' '.join(txt_list[i:n+i]) for i in range(len(txt_list)-n+1)]
    return ngram

txt = 'I am an NLPer'
n = 2
print(n_gram(txt,n))
