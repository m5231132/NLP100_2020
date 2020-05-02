import re

def tab_replece(row):
  row = re.sub('\t',' ',row)
  return row

with open('popular-names.txt','r') as f:
      docx = f.read().split('\n')
      for doc in docx:
          print(tab_replece(doc))