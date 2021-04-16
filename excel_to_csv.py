import pandas as pd
import numpy as np
import glob

all_files=[]

#Colectando todos los archivos
for f in glob.glob('/Users/wilmontenegro/Downloads/*.xls*'):
    df=pd.read_excel(f)
    df.iloc[[0,1]]
    print(f'El total de filas del archivo {f[31::]} es:', df.shape[0])
    all_files.append(pd.read_excel(f))

df = pd.concat(all_files, ignore_index='True')
print(df.head(10))
print(f'El total de filas consolidadas es', df.shape[0])

#Para exportar a Excel
save_excel = pd.ExcelWriter('/Users/wilmontenegro/Downloads/Todo.xlsx')
df.to_excel(save_excel,'Data_Total')
save_excel.save()

#Para exportar a CSV
#save_csv = pd.DataFrame(df)
#save_csv.to_csv('/Users/wilmontenegro/Downloads/Todo.csv', index = None, header=True)



