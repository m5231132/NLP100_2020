with open('popular-names.txt','r') as f:
    doc = f.readlines()
    cnt = 0
    for _ in doc:
        cnt += 1

print(cnt)
