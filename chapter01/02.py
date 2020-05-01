txt1 = 'パトカー'
txt2 = 'タクシー'
txt_list = [t1+t2 for t1, t2 in zip(txt1, txt2)]
print(''.join(txt_list))
