doc = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
vocab = [len(w) - w.count(',') - w.count('.') for w in doc.split(' ')]
print(vocab)
