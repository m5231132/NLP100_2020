txt = 'パタトクカシーー'
hoge = [txt[i] for i in range(len(txt)) if i%2!=0]
print("".join(hoge))
