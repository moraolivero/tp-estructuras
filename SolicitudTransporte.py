
import csv 
from typing import Dict, List
from Nodo import Nodo

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
        self.identificacion_carga = identificacion_carga
        self.peso_carga = peso_carga
        self.nodo_origen = nodo_origen
        self.nodo_destino = nodo_destino

    @staticmethod
    def leer_csv(nombre_archivo: str, nodos: Dict[str, Nodo])->List['SolicitudTransporte']:
        """Carga solicitudes desde un archivo CSV dado un diccionario de nodos."""
        solicitudes=[] 
        with open (nombre_archivo, newline='') as archivo: 
            lector= csv.reader (archivo)
            next(lector)
            for linea in lector:
                if len(linea) != 4:
                    print(f" Error en los datos de solicitud: {linea}")
                    continue 
                ident= linea[0]
                peso= float(linea[1])
                origen=nodos.get(linea[2])
                destino= nodos.get(linea[3])
                if origen is None or destino is None:
                    raise ValueError (f'Nodo invalido')
                solicitud=SolicitudTransporte(ident, peso, origen, destino)
                solicitudes.append(solicitud)
        return solicitudes 

