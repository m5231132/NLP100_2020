def cipher(word):
    processed_code = ''
    for i in range(len(word)):
        if word[i].islower():
            code = chr(219 - ord(word[i]))
        else:
            code = word[i]

        processed_code += code

    return processed_code
doc = 'Natural Language Processing'
print('Encode : {} → {}'.format(doc, cipher(doc)))
print('Decode : {} → {}'.format(cipher(doc), cipher(cipher(doc))))
