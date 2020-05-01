x = 'paraparaparadise'
y = 'paragraph'
n = 2 
X = set([x[i:n+i] for i in range(len(x)-n+1)])
Y = set([y[i:n+i] for i in range(len(y)-n+1)])

union_X_Y = X.union(Y)
intersection_X_Y = X.intersection(Y)
difference_X_Y = X.difference(Y)
print(union_X_Y)
print(intersection_X_Y)
print(difference_X_Y)
print('se' in X)
print('se' in Y)
