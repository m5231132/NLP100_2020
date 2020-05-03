import sys
import pandas as pd

arv = sys.argv
n = int(arv[1])
df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)

print(df.tail(n))
