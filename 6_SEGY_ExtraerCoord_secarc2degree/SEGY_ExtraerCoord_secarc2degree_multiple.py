# -*- coding: utf-8 -*-
"""
Creado por Sebastian Principi y Federico Esteban
28-09-2022 
Extrae las coordendas de las trazas y las guarda en archivos csv como 
grados decimales y con los datos del FFID (byte 9 del trace header).
Bytes 73 y 77 estan en SEGUNDOS DE ARCO.
GENERA UN CSV POR CADA SEGY
"""

# Variables a modificar
# --------------------------------------------------------------
# Directorio a analizar
#path=r"C:\Users\usuario\Desktop\Nueva carpeta"
path=r"/home/federico/Github/Geoflama/SEGY/0_DatosPrueba"

# Inicio Script
# --------------------------------------------------------------
# 0. Importar librerias
import os
import segyio
import pandas as pd

# 1. Cambiar al directorio path 
os.chdir(path)

# 2. Hacer un loop para cada archivo
for file in os.listdir(path):
    
    # A. Abir todos los .sgy de la carpeta.
    if file.endswith(".sgy"):
        input_=str(file)
        
        # B. Abrir el archivo como read write
        with segyio.open(input_, "r+", ignore_geometry=True) as f:
            
            # C. Leer los header de X e Y y los paso de segundos de arco a grados
            factor=3600000
            sourceX = f.attributes(segyio.TraceField.SourceX)[:]/factor
            sourceY = f.attributes(segyio.TraceField.SourceY)[:]/factor

            # Leer datos de FFID (byte 9)
            ffid = f.attributes(segyio.TraceField.FieldRecord)[:]
    
            # D. Imprimir en la terminal
            print(sourceX)
            print(sourceY)
            print (ffid)

        # E. Convierto las listas de valores a un dataframe
        df = pd.DataFrame(list(zip(sourceX, sourceY, ffid)),columns =['#Long', 'Lat', "FFID"])
        
        # F. Guardo los datos como archivos de texto (uno por cada segy) en un CSV
        df.to_csv(input_+".csv", index=False,sep=",")