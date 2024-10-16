import pandas as pd
from datetime import datetime


file_path = './Practicas.xlsx'
sheet_name = 'DatosPrueba'


df = pd.read_excel(file_path, sheet_name=sheet_name)


masculino_df = df[df['Gender'] == 'Male']  
femenino_df = df[df['Gender'] == 'Female']


masculino_df = masculino_df[['Business Unit', 'Job Title', 'Full Name', 'Age', 'Hire Date']]
femenino_df = femenino_df[['Business Unit', 'Job Title', 'Full Name', 'Age', 'Hire Date']]


fecha_actual = datetime.now().strftime('%Y%m%d')


archivo_masculino = f'./{fecha_actual}_personal_masculino.txt'
archivo_femenino = f'./{fecha_actual}_personal_femenino.txt'


masculino_df.to_csv(archivo_masculino, sep=';', index=False)
femenino_df.to_csv(archivo_femenino, sep=';', index=False)

print(f"Archivos generados: {archivo_masculino} y {archivo_femenino}")
