
import csv 
from typing import Dict, List
from Nodo import Nodo
from collections import deque

class SolicitudTransporte:
    """Representa una solicitud de transporte con carga y nodos origen/destino."""
    def __init__(
        self,
        identificacion_carga: str,
        peso_carga: float,
        nodo_origen: Nodo,
        nodo_destino: Nodo,
    ):
        """Inicializa la solicitud con identificador, peso y nodos."""
        if not isinstance(identificacion_carga, str):
            raise ValueError("La identificación de carga debe ser una cadena de texto.")
        if not isinstance(peso_carga, (int, float)) or peso_carga <= 0:
            raise ValueError("El peso de la carga debe ser un número positivo.")
        if not isinstance(nodo_origen, Nodo) or not isinstance(nodo_destino, Nodo):
            raise TypeError("Los nodos origen y destino deben ser instancias de Nodo.")
        self.identificacion_carga = identificacion_carga
        self.peso_carga = peso_carga
        self.nodo_origen = nodo_origen
        self.nodo_destino = nodo_destino

    @staticmethod
    def leer_csv(nombre_archivo: str, nodos: Dict[str, Nodo]) -> deque:
        """Carga solicitudes desde un archivo CSV dado un diccionario de nodos."""
        if not isinstance(nombre_archivo, str):
            raise TypeError("El nombre del archivo debe ser una cadena de texto.")
        if not nombre_archivo.endswith('.csv'):
            raise ValueError("El nombre del archivo debe terminar con '.csv'.")
        if not isinstance(nodos, dict):
            raise TypeError("Los nodos deben ser un diccionario con nombre como clave y Nodo como valor.")
        for clave, valor in nodos.items():
            if not isinstance(valor, Nodo):
                raise TypeError(f"El valor para la clave '{clave}' no es un Nodo.")
        solicitudes = deque()
        with open(nombre_archivo, newline='') as archivo:
            lector = csv.reader(archivo)
            next(lector)
            for linea in lector:
                if len(linea) != 4:
                    print(f"Error en los datos de solicitud: {linea}")
                    continue
                ident = linea[0]
                peso = float(linea[1])
                origen = nodos.get(linea[2])
                destino = nodos.get(linea[3])
                if origen is None or destino is None:
                    raise ValueError(f'Nodo invalido')
                solicitud = SolicitudTransporte(ident, peso, origen, destino)
                solicitudes.append(solicitud)
        return solicitudes
    
 