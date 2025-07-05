
import csv
from typing import Dict
from Nodo import Nodo, Conexion
from Itinerario import Itinerario
import matplotlib.pyplot as plt

def cargar_nodos_desde_csv(ruta:str)-> Dict[str, Nodo]:
    """Carga nodos desde un archivo CSV y retorna un diccionario nombre->Nodo."""
    nodos={}
    with open(ruta, newline='') as archivo:
        lector=csv.reader(archivo)
        next(lector)
        for fila in lector:
            if len(fila) != 1:
                print(f" Error en los datos: {fila}")
                continue
            nombre = fila[0]
            nodo = Nodo(nombre) 
            nodos[nombre]=nodo
    return nodos

def cargar_conexiones_desde_csv(ruta:str, nodos: Dict[str, Nodo]) -> None:
    """Carga conexiones desde CSV y las agrega a los nodos correspondientes."""
    with open(ruta, newline='') as archivo:
        lector=csv.reader(archivo)
        next(lector)
        for fila in lector:
            if len(fila) != 6:
                print(f" Error en los datos: {fila}")
                continue
            origen, destino, modo, distancia, restriccion, valor = fila
            if origen not in nodos or destino not in nodos:
                raise ValueError(f'Origen o destino no encontrado en nodos: {fila}')
            conexion = Conexion(
                origen=nodos[origen],
                destino=nodos[destino],
                modo=modo,
                distancia_km=float(distancia),
                restriccion=restriccion if restriccion else None,
                valor_restriccion=valor if valor else None
            )
            nodos[origen].agregar_conexion(conexion)



def graficar_distancia_vs_tiempo(itinerario: Itinerario):
    """Grafica distancia acumulada frente a tiempo acumulado del itinerario."""
    distancias = []
    tiempos = []
    tiempo_acumulado = 0
    distancia_acumulada = 0
    for tramo in itinerario.tramos:
        distancia_acumulada += tramo.conexion.distancia_km
        tiempo_acumulado += tramo.calcular_tiempo()
        distancias.append(distancia_acumulada)
        tiempos.append(tiempo_acumulado)

    plt.plot(tiempos, distancias, marker='o')
    plt.xlabel("Tiempo acumulado (horas)")
    plt.ylabel("Distancia acumulada (km)")
    plt.title("Distancia vs. Tiempo")
    plt.grid(True)
    plt.show()

def graficar_costo_vs_distancia(itinerario: Itinerario):
    """Grafica costo acumulado frente a distancia acumulada del itinerario."""
    distancias = []
    costos = []
    costo_acumulado = 0
    distancia_acumulada = 0
    for tramo in itinerario.tramos:
        distancia_acumulada += tramo.conexion.distancia_km
        costo_acumulado += tramo.calcular_costo_sin_kg()
        distancias.append(distancia_acumulada)
        costos.append(costo_acumulado)

    plt.plot(distancias, costos, marker='o')
    plt.xlabel("Distancia acumulada (km)")
    plt.ylabel("Costo acumulado ($)")
    plt.title("Costo vs. Distancia")
    plt.grid(True)
    plt.show()
