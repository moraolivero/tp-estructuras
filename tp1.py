import csv
from typing import List, Dict, Set, Optional


class Nodo:
    """
    Voy a tener para cada nodo:
        - nombre  'Azul'
        - conexiones: List['Conexion'] :  Hasta Junin 265km, Hasta mar del plata 246km, ...
        - modos_disponibles: modos disponibles de trasnporte  Ejemplo: {"Ferroviario", "Maritimo", "Automotor", "Aereo"}
    """

    def __init__(self, nombre: str, modos_disponibles: Set[str]):
        self.nombre = nombre
        self.modos_disponibles = modos_disponibles
        self.conexiones: List["Conexion"] = []

    def agregar_conexion(self, conexion: "Conexion"):
        self.conexiones.append(conexion)

    def __str__(self):  # print(nodo)
        return self.nombre


class Conexion:  # docstrings --> documentation string --> string de documentacion
    """
    Conexion va a tomar:
        - origen: de donde viene, por ejemplo de Junin
        - destino: a donde va, por ejemplo a Zarate
        - modo: el medio de transporte por el cual hago ese recorrido
            - en el esquema dado en la pagina 8, entre Junin y Zarate voy a tener
            una conexion para la red automotor y la red ferroviaria, pero no para
            la maritima y la aerea.
        - distancia_km: distancia

    Ejemplo de una instancia:

    Conexion(nodo_junin, nodo_zarate, 'automotor')
    """

    def __init__(
        self, origen: Nodo, destino: Nodo, modo: str, distancia_km: float
    ):  # TODO: faltan agregar parametros como la velocidad maxima, peso maximo (opcional, se puede usar una tabla definida en otra parte)
        self.origen = origen
        self.destino = destino
        self.modo = modo
        self.distancia_km = distancia_km

    def __str__(self):
        return f"{self.origen}  -> {self.destino} ({self.modo}, {self.distancia_km} km)"  # printear Junin -> Zarate ('automotor', 185 km)


class Vehiculos:
    tipo_vehiculo = ["Ferroviario", "Maritimo", "Automotor", "Aereo"]

    def __init__(
        self,
        modo: str,
        velocidad: int,
        capacidad: int,
        costo_fijo: float,
        costo_x_km: float,
        costo_x_kg: float,
    ):
        self.modo = modo
        self.velocidad = velocidad
        self.capacidad = capacidad
        self.costo_fijo = costo_fijo
        self.costo_x_km = costo_x_km
        self.costo_x_kg = costo_x_kg

    def validar_int(dato):
        try:
            dato = int(dato)
        except TypeError:
            raise TypeError("El dato ingresado no es un numero entero")

    def validar_float(dato):
        try:
            dato = float(dato)
        except TypeError:
            raise TypeError("El dato ingresado no es un numero valido")

    @classmethod
    def validar_modo(cls, modo: str):
        if modo not in cls.tipo_vehiculo:
            return False
        else:
            return True


# class Ferroviario(Vehiculos):
#     def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
#         super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)


# class Maritimo(Vehiculos):
#     def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
#         super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)


# class Automotor(Vehiculos):
#     def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
#         super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)


# class Aereo(Vehiculos):
#     def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
#         super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)


# class Camino:
#     def __init__(
#         self,
#     ):
#         pass

class SolicitudTransporte:
    def __init__(self, identificacion_carga: str, pero_carga: float , nodo_origen: Nodo, nodo_destino: Nodo):

        pass
    def leer_csv(nombre_archivo):
        datos = []
        
        with open(nombre_archivo, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            archivo.readline()
            for linea in lector_csv:
                datos.append(linea)
        return datos
        


"""
class SolicitudTransporte() que tome
    ● Identificación de la Carga.
    ● Peso de la Carga: kilogramos (kg).
    ● Nodo de Origen: La ciudad donde se recoge la carga.
    ● Nodo de Destino: La ciudad final donde se debe entregar la carga

class TramoItinerario
    ● conexion
    ● vehiculo (tipo vehiculo)
    ● carga  (en kg)

    metodos: 
        - calcular_tiempo
        - calcular_costo

class Itinerario
    ● tramos: Lista de TramoItinerario
    ● kpi: str  'costo' o 'tiempo'
    
    metodos:
        - tiempo_total
        - costo_total
        - mostrar_resumen
"""
