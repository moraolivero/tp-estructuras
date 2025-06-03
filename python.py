import csv
nombre_csv = ''
def leer_csv(nombre_archivo):
    carga = []
    
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        archivo.readline()
        for linea in lector_csv:
            carga.append(linea)
    return datos