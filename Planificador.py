
from Vehiculos import Vehiculos
from typing import List, Optional
from Nodo import Nodo
from Itinerario import Itinerario
from TramoItinerario import TramoItinerario
import math


class Planificador:
    """Clase para planificar itinerarios óptimos según costo o tiempo."""
    def __init__(self, vehiculos: List[Vehiculos]):
        """Inicializa con la lista de vehículos disponibles."""
        self.vehiculos = vehiculos

    def buscar_mejor_itinerario(
        self,
        nodo_actual: Nodo,
        nodo_destino: Nodo,
        carga: float,
        kpi: str,
        visitados: List[Nodo],
        tramos_actuales: List["TramoItinerario"],
        modo_en_uso:Optional[str]=None
    ) -> Optional["Itinerario"]:
        """Busca recursivamente el mejor itinerario según el KPI indicado."""
        if nodo_actual == nodo_destino:
            return Itinerario(tramos_actuales, kpi)
    
        
        mejores_itinerarios = []

        visitados.append(nodo_actual)
        
        for conexion in nodo_actual.conexiones:
            if not conexion.validar_carga(carga):
                continue

            siguiente_nodo = conexion.destino
            if siguiente_nodo in visitados:
                continue

            if not conexion.validar_modo(modo_en_uso):
                continue

            vehiculos_compatibles = [
                v for v in self.vehiculos if v.modo == conexion.modo
            ]

            for vehiculo in vehiculos_compatibles:
                cantidad_vehiculos = math.ceil(carga/ vehiculo.capacidad)
                if cantidad_vehiculos <=0:
                    continue
                tramo = TramoItinerario(conexion, vehiculo, carga)
                nuevo_tramo = tramos_actuales + [tramo]
                itinerario = self.buscar_mejor_itinerario(
                    siguiente_nodo, nodo_destino, carga, kpi, visitados.copy(), nuevo_tramo, modo_en_uso or conexion.modo
                )

                if itinerario:
                    mejores_itinerarios.append(itinerario)

        if not mejores_itinerarios:
            return None

        if kpi == "tiempo":
            return min(mejores_itinerarios, key=lambda i: i.tiempo_total())
        elif kpi == "costo":
            return min(mejores_itinerarios, key=lambda i: i.costo_total())
        else:
            raise ValueError("KPI inválido. Debe ser 'tiempo' o 'costo'.")


    def planificar_itinerario(
        self,
        nodo_origen: Nodo,
        nodo_destino: Nodo,
        carga: float,
        kpi: str
    ) -> Optional["Itinerario"]:
        """Inicia la planificación del itinerario desde origen a destino."""
        return self.buscar_mejor_itinerario(
            nodo_origen,
            nodo_destino,
            carga,
            kpi,
            visitados=[],
            tramos_actuales=[],
            modo_en_uso=None
        )