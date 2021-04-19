import pandas as pd
import numpy as np
import glob

all_files=[]
columns_preliquidacion = ['CIA','FCH_PROCESO','PEDIDO','ZONA','CODCLIENTE','APELLIDOS','NOMBRE1','NOMBRE2','DIRECCION','TELEFONO','DEPART','PROV','DISTRITO' ]
columns_prueba_entrega = ['Fecha Facturación', 'Fecha Promesa Entrega', 'Fecha Entrega', 'Compañía', 'Campaña', 'Zona', '# Orden', 'Código Consultora', 'Nombre Consultora', 'Estado Orden', 'Observaciones', 'Imágenes']

#Colectando todos los archivos, index_Col es para que no ponga un index por defecto, header para seleccionar en que fila estan los titulos
for f in glob.glob('/Users/wilmontenegro/Downloads/*.xls*'):
    df=pd.read_excel(f, header=1, usecols=columns_prueba_entrega)
    print(f'El total de filas del archivo {f[31::]} es:', df.shape[0])
    all_files.append(pd.read_excel(f, header=1, usecols=columns_prueba_entrega))

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



