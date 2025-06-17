from tpprueba import (
    cargar_nodos_desde_csv,
    cargar_conexiones_desde_csv,
    SolicitudTransporte,
    Planificador,
    Ferroviario,
    Automotor,
    Maritimo,
    Aereo,
    graficar_distancia_vs_tiempo,
)

def main():
    # === Rutas ===
    ruta_nodos = "archivos_ejemplo/archivos_ejemplo/nodos.csv"
    ruta_conexiones = "archivos_ejemplo/archivos_ejemplo/conexiones.csv"
    ruta_solicitudes = "archivos_ejemplo/archivos_ejemplo/solicitudes.csv"

    # === Cargar red de transporte ===
    nodos = cargar_nodos_desde_csv(ruta_nodos)
    cargar_conexiones_desde_csv(ruta_conexiones, nodos)

    # === Vehículos disponibles ===
    vehiculos = [
        Ferroviario(100, 150000, 100, 20, 3),
        Automotor(80, 30000, 30, 5, 1),
        Maritimo(40, 100000, 500, 15, 2),
        Aereo(600, 5000, 750, 40, 10),
    ]
    planificador = Planificador(vehiculos)

    # === Cargar solicitudes ===
    solicitudes = SolicitudTransporte.leer_csv(ruta_solicitudes, nodos)

    # === Procesar solicitudes ===
    for solicitud in solicitudes:
        print(f"\n Solicitud: {solicitud.identificacion_carga}")
        print(" KPI: Tiempo")
        it_tiempo = planificador.planificar_itinerario(
            solicitud.nodo_origen, solicitud.nodo_destino, solicitud.peso_carga, "tiempo"
        )
        if it_tiempo:
            print(it_tiempo)
            graficar_distancia_vs_tiempo(it_tiempo)
        else:
            print(" No se encontró itinerario por tiempo.")

        print(" KPI: Costo")
        it_costo = planificador.planificar_itinerario(
            solicitud.nodo_origen, solicitud.nodo_destino, solicitud.peso_carga, "costo"
        )
        if it_costo:
            print(it_costo)
            graficar_distancia_vs_tiempo(it_costo)
        else:
            print(" No se encontró itinerario por costo.")

if __name__ == "__main__":
    main()

'''
nodo_junin = Nodo("Junin", {"Ferroviario", "Automotor", "Aereo"})
nodo_zarate = Nodo("Zarate", {"Ferroviario", "Automotor", "Maritimo"})


print("Printeo nodo Zarate: ")
print(nodo_zarate)
print(nodo_zarate.modos_disponibles)
print()

print("Printeo nodo Junin: ")
print(nodo_junin)
print(nodo_junin.modos_disponibles)
print()


print("Agrego esta conexion: ")
conexion_junin_a_zarate = Conexion(nodo_junin, nodo_zarate, "Automotor", 185)
nodo_junin.agregar_conexion(conexion_junin_a_zarate)

conexion1 = nodo_junin.conexiones[0]
print(conexion1)


print("Agrego la conexion opuesta: ")
conexion_zarate_a_junin = Conexion(nodo_zarate, nodo_junin, "Automotor", 185)
nodo_zarate.agregar_conexion(conexion_zarate_a_junin)

conexion1 = nodo_zarate.conexiones[0]
print(conexion1)

#####################


def main():
    ruta_nodos = 'nodos.csv'
    ruta_conexiones = 'conexiones.csv'
    nodos = tp1.cargar_nodos_desde_csv(ruta_nodos)
    tp1.cargar_conexiones_desde_csv(ruta_conexiones, nodos)
    
    # Mostrar la red para verificar que se cargó bien
    print("Nodos cargados:")
    for nodo in nodos.values():
        print(nodo)
        for conexion in nodo.conexiones:
            print("  ", conexion)

if __name__ == '__main__':
    main()

'''


