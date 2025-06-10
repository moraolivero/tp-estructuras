


# lo que hizo chat: 

import matplotlib.pyplot as plt

def graficar_distancia_vs_tiempo(itinerario):
    tiempos = []
    distancias = []
    tiempo_acum = 0
    distancia_acum = 0

    for tramo in itinerario.tramos:
        tiempo_acum += tramo.calcular_tiempo()
        distancia_acum += tramo.conexion.distancia_km
        tiempos.append(tiempo_acum)
        distancias.append(distancia_acum)

    plt.figure(figsize=(8, 5))
    plt.plot(tiempos, distancias, marker='o')
    plt.title("Distancia Acumulada vs. Tiempo Acumulado")
    plt.xlabel("Tiempo acumulado (horas)")
    plt.ylabel("Distancia acumulada (km)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def graficar_costo_vs_distancia(itinerario):
    costos = []
    distancias = []
    costo_acum = 0
    distancia_acum = 0

    for tramo in itinerario.tramos:
        costo_acum += tramo.calcular_costo()
        distancia_acum += tramo.conexion.distancia_km
        costos.append(costo_acum)
        distancias.append(distancia_acum)

    plt.figure(figsize=(8, 5))
    plt.plot(distancias, costos, marker='s', color='orange')
    plt.title("Costo Acumulado vs. Distancia Acumulada")
    plt.xlabel("Distancia acumulada (km)")
    plt.ylabel("Costo acumulado ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()