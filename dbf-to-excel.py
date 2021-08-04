import glob
import pandas as pd
from dbfread import DBF

print('.:Nombres de los archivos locales de la carpeta:.')
archivos=glob.glob('*.DBF')
print(archivos)

for i in archivos:
    print('.:Convirtiendo DBF a dataframe:. ',i)
    table = DBF(i,load=True,encoding='latin-1')

    frame = pd.DataFrame(iter(table))
    nombre_de_salida=i.replace('.DBF','')+".xlsx";
    frame.to_excel(nombre_de_salida, index=False) 
