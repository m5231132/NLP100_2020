doc = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
vocab = doc.split(' ')
index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dic = {}
for i, word in enumerate(vocab):
    if i+1 in index:
        dic.update({i : word[0]})
    else:
        dic.update({i : word[:2]})
print(dic)
