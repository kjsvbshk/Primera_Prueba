import os
import pandas as pd

print("Ruta actual de trabajo:", os.getcwd())

file_path = './Practicas.xlsx'
sheet_name = 'DatosPrueba'

df = pd.read_excel(file_path, sheet_name=sheet_name)

df['duplicados'] = df.duplicated(keep=False)

df['duplicados'] = df['duplicados'].replace({True: 'X', False: ''})

output_file_path = './Nueva_Practicas.xlsx'
df.to_excel(output_file_path, index=False)

print("Los duplicados han sido marcados y guardados en el nuevo archivo.")
