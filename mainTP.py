
from SolicitudTransporte import SolicitudTransporte
from Planificador import Planificador
from utils import (
    cargar_nodos_desde_csv,
    cargar_conexiones_desde_csv,
    graficar_distancia_vs_tiempo,
    graficar_costo_vs_distancia,
)
from Ferroviaria import Ferroviaria
from Maritimo import Maritimo
from Automotor import Automotor
from Aerea import Aerea
import sys
def main():
    try:
        # 1. Cargar nodos
        nodos = cargar_nodos_desde_csv("nodos.csv")

        # 2. Cargar conexiones
        cargar_conexiones_desde_csv("conexiones.csv", nodos)

        # 3. Definir vehículos
        vehiculos = [
            Ferroviaria('Ferroviaria', 100, 150000, 100, 20, 3),
            Maritimo('Maritimo', 40, 100000, 500, 15, 2),
            Automotor('Automotor', 80, 30000, 30, 5, 1),
            Aerea('Aerea', 600, 5000, 750, 40, 10),
            ]
        

        # 4. Cargar solicitudes
        solicitudes = SolicitudTransporte.leer_csv("solicitudes.csv", nodos)

        # 5. Crear planificador
        planificador = Planificador(vehiculos)

        # 6. Procesar cada solicitud con ambos KPIs
        while solicitudes:
            solicitud = solicitudes.popleft()
            print(f"\n=== Solicitud: {solicitud.identificacion_carga} ===")
            print(f"Origen: {solicitud.nodo_origen.nombre}")
            print(f"Destino: {solicitud.nodo_destino.nombre}")
            print(f"Peso: {solicitud.peso_carga} kg")

            for kpi in ["costo", "tiempo"]:
                print(f"\n--- Optimización por {kpi.upper()} ---")
                itinerario = planificador.planificar_itinerario(
                    solicitud.nodo_origen,
                    solicitud.nodo_destino,
                    solicitud.peso_carga,
                    kpi
                )

                if itinerario:
                    print(itinerario)
                    graficar_distancia_vs_tiempo(itinerario)
                    graficar_costo_vs_distancia(itinerario)

                else:
                    print("No se encontró un itinerario válido.")

    except FileNotFoundError as e:
        print(f" Archivo no encontrado: {e.filename}")
        
    except ValueError as e:
        print(f" Error en los datos: {e}")
    except Exception as e:
        print(f" Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
