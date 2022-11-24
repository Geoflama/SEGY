# Procesamientos simples de SEGY

Realizar procesamientos simples de archivos SEG-Y que incluyen:
Los scripts NO incluyen el procesamiento de los datos.

1. Extracción de los datos de un unica traza.
2. Separar SEG-Y
3. Unir SEG-Y
4. Editar el Text Header.
5. Extraer y convertir datos de navegacion.

## Programas a utilizar

Como introducción se sugiere leer:
* Formato de archivos SEG-Y. Se asume que tienen el formato original. 
* Funcionamiento del programa **dd**.

## Lista de Scripts

1. SEGY_Extract_TraceData.sh
2. SEGY_Sobreescribir_TextHeader.sh
3. SEGY_Extraer.sh
4. SEGY_Unir_Batch.sh
5. 


## Mas informacion
* Formato SEGY version 1. https://pubs.usgs.gov/of/2001/of01-326/HTML/FILEFORM.HTM
* Formato SEG-Y: Hagelund (2017) https://seg.org/Portals/0/SEG/News%20and%20Resources/Technical%20Standards/seg_y_rev2_0-mar2017.pdf
* Explicacion del programa **dd** en Wikipedia: https://es.wikipedia.org/wiki/Dd_(Unix)
