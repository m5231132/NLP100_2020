col1 = open('col1.txt', 'r')
col2 = open('col2.txt', 'r')

cl1 = col1.read().split('\n')
cl2 = col2.read().split('\n')

for c1, c2 in zip(cl1, cl2):
    print(c1+'\t'+c2)