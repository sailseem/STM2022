
import re
import pandas as pd
import numpy as np

protein=pd.read_csv('list.txt',encoding='utf-8')
protein=np.array(protein.iloc[:,0])
protein

with open('library.fasta', 'r') as f:
    data = f.read()

m = data.split('>')

list_data = []
for i in m:
    if i:
        l = i.split('\n')
        try:
            data1 = l[0].split('|')[1]
            data2 = l[0].split('GN=')[1].split(' ')[0]
        except:
            data1 =''
            data2 =''
        
        data3 = ''.join(l[1:])
        data = {
            'data1':data1,
            'data2':data2,
            'data3':data3}
        list_data.append(data)
df = pd.DataFrame(list_data)    

df = df.drop_duplicates('data1').set_index('data1')  

result = df.reindex(protein).dropna()
result.to_csv('result.csv')
result