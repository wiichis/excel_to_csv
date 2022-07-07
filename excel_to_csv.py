import pandas as pd
import numpy as np
import glob

all_files=[]

# columns_preliquidacion = ['Fecha Plan','Código del Vehículo','Código de Orden','Código de Dirección','Dirección','Nombre Cliente','Comuna',
#                            'Código Postal','Lat','Lng','Estado','Motivo','Hora de Entrega','PdE cercano a dirección',
#                            'Distancia PdE','PdE lat','PdE lng','Conductor','Orden de entrega','Orden original','Tiene imágenes',
#                            'Tiempo de servicio','Duración de la detención','ETA iniciado']

#Listas de Campos Beetrack
#columns_preliquidacion = ['Código de Orden','Lat','Lng','Dirección','Descripción Item','Unidades','Código de Dirección','Nombre dirección','Comuna']

#Analisis Km
columns_preliquidacion = ['Nombre Plan','Fecha Plan','Código de Orden','Grupo de Flota','Código del Vehículo','Descripción del Vehículo','Odómetro','Código de Dirección',
                          'Nombre Cliente','Comuna','Código Postal','Lat','Lng','Estado','Motivo','Hora de Entrega','PdE cercano a dirección','Distancia PdE','PdE lat',
                          'PdE lng','Conductor','Hora inicio ruta','Hora fin ruta','Código de ruta','Orden de entrega','Orden original','Duración de la detención']


#Prueba de Entrega
#columns_preliquidacion = ['Código de Orden', 'Estado', 'Motivo', 'Hora de Entrega']

columns_prueba_entrega_belcorp = ['Fecha Facturación', 'Fecha Promesa Entrega', 'Fecha Entrega',
                                  'Compañía', 'Campaña', 'Zona', 
                                  '# Orden', 'Código Consultora', 
                                  'Nombre Consultora', 'Estado Orden', 
                                  'Observaciones', 'Imágenes']

#Para exportar a Excel
def export_excel():
    save_excel = pd.ExcelWriter('/Users/wilmontenegro/Downloads/Todo.xlsx')
    df.to_excel(save_excel,'Data_Total')
    save_excel.save()

#Para exportar a CSV
def export_csv():
    save_csv = pd.DataFrame(df)
    save_csv.to_csv('/Users/wilmontenegro/Downloads/Todo.csv', index = None, header=True)

def selection_type_read():
    global archive_type, header_type, user_selection_type_export
    print('1 -> Preliquidación \n2 -> Prueba de Entrega')
    user_selection_type_read = int(input("Selecciona el tipo de archivo: "))
    print('1 -> Excel \n2 -> CSV')
    user_selection_type_export = int(input("Selecciona en que formato quieres exportar: "))
    
    if  user_selection_type_read == 1:
        archive_type = columns_preliquidacion
        header_type = 0
    elif user_selection_type_read == 2:
        archive_type = columns_prueba_entrega_belcorp
        header_type = 1
    
def selection_type_export():
    if user_selection_type_export == 1:
        export_excel()
    elif user_selection_type_export == 2:
        export_csv()
    

#Colectando todos los archivos, header para seleccionar en que fila estan los titulos
def read():
    global df
    for f in glob.glob('/Users/wilmontenegro/Downloads/Consolidar/*.xls*'):
        df=pd.read_excel(f, header=header_type, usecols = archive_type)
        print(f'El total de filas del archivo {f[31::]} es:', df.shape[0])
        all_files.append(pd.read_excel(f, header=header_type, usecols = archive_type))

    df = pd.concat(all_files, ignore_index='True')
    print(df.head(10))
    print(f'El total de filas consolidadas es', df.shape[0])


def run():
    selection_type_read()
    read()
    selection_type_export()


if __name__=='__main__':
    run()
