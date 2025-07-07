
from Vehiculos import Vehiculos
from typing import List, Optional
from Nodo import Nodo
from Itinerario import Itinerario
from TramoItinerario import TramoItinerario
import math
from typing import Set, Dict, List
from collections import deque
from collections import defaultdict

class Planificador:
    """Clase que gestiona la planificación de itinerarios óptimos entre nodos, según tiempo o costo."""
    KPI_VALIDOS = {"tiempo", "costo"}

    def __init__(self, vehiculos: List[Vehiculos]):
        """Inicializa el planificador con una lista de vehículos disponibles, agrupados por modo de transporte."""
        if not isinstance(vehiculos, list):
            raise TypeError("Vehículos debe ser una lista.")
        for v in vehiculos:
            if not isinstance(v, Vehiculos):
                raise TypeError("Todos los elementos de la lista deben ser instancias de Vehiculos.")
        self.vehiculos_por_modo: Dict[str, List[Vehiculos]] = defaultdict(list)
        for vehiculo in vehiculos:
            self.vehiculos_por_modo[vehiculo.modo].append(vehiculo)

    def buscar_mejor_itinerario(self, nodo_actual, nodo_destino, carga, kpi, visitados: Set, tramos_actuales: deque, modo_en_uso: Optional[str] = None):
        """Algoritmo recursivo que busca el mejor itinerario desde nodo_actual hasta nodo_destino."""
        if nodo_actual == nodo_destino:
            return Itinerario(list(tramos_actuales), kpi)

        mejores_itinerarios = []
        visitados.add(nodo_actual)

        for conexion in nodo_actual.conexiones:
            if not conexion.validar_carga(carga):
                continue
            siguiente_nodo = conexion.destino
            if siguiente_nodo in visitados:
                continue
            if not conexion.validar_modo(modo_en_uso):
                continue

            vehiculos_compatibles = self.vehiculos_por_modo.get(conexion.modo, [])
            for vehiculo in vehiculos_compatibles:
                cantidad_vehiculos = math.ceil(carga / vehiculo.capacidad)
                if cantidad_vehiculos <= 0:
                    continue
                tramo = TramoItinerario(conexion, vehiculo, carga)
                tramos_actuales.append(tramo)
                itinerario = self.buscar_mejor_itinerario(
                    siguiente_nodo, nodo_destino, carga, kpi, visitados.copy(), tramos_actuales, modo_en_uso or conexion.modo
                )
                tramos_actuales.pop()
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

    def planificar_itinerario(self, nodo_origen, nodo_destino, carga, kpi):
        """Inicia la planificación del itinerario desde origen a destino según el KPI seleccionado."""
        if not isinstance(nodo_origen, type(nodo_destino)):
            raise TypeError("Los nodos deben ser instancias del mismo tipo.")
        if not isinstance(carga, (int, float)) or carga <= 0:
            raise ValueError("La carga debe ser un número positivo.")
        if kpi not in self.KPI_VALIDOS:
            raise ValueError(f"KPI inválido. Debe ser uno de {self.KPI_VALIDOS}.")
        return self.buscar_mejor_itinerario(nodo_origen, nodo_destino, carga, kpi, visitados=set(), tramos_actuales=deque(), modo_en_uso=None)
