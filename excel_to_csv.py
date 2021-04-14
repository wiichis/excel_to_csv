import pandas as pd
import numpy as np
import glob

all_files=[]

#Colectando todos los archivos
for f in glob.glob('/Users/wilmontenegro/Downloads/*.xlsx'):
    df=pd.read_excel(f)
    all_files.append(pd.read_excel(f))

df = pd.concat(all_files, ignore_index='True')
print(df.head(10))

#Para exportar a Excel
#save_excel = pd.ExcelWriter('/Users/wilmontenegro/Downloads/Todo.xlsx')
#df.to_excel(save_excel,'Hoja 1')
#save_excel.save()

#Para exportar a CSV
save_csv = pd.DataFrame(df)
save_csv.to_csv('/Users/wilmontenegro/Downloads/Todo.csv', index = None, header=True)



