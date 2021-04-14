import pandas as pd
import numpy as np
import glob

all_files=[]

for f in glob.glob("*.xlsx"):
    df=pd.read_excel(f)
    all_files.append(pd.read_excel(f))

df = pd.concat(all_files, ignore_index='True')
print(df.head(10))

save_excel = pd.ExcelWriter('Todo.xlsx')
df.to_excel(save_excel,'Hoja 1')
save_excel.save()

#read_file = pd.read_excel (r'Path where the Excel file is stored\File name.xlsx')
#read_file.to_csv (r'Path to store the CSV file\File name.csv', index = None, header=True)

