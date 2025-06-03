import csv
import math
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
        
class Planificador:
    def __init__(self):
        self



class SolicitudTransporte:
    def __init__(self, identificacion_carga: str, peso_carga: float , nodo_origen: Nodo, nodo_destino: Nodo):
        self.identificacion_carga=identificacion_carga
        self.peso_carga=peso_carga
        self.nodo_origen=nodo_origen
        self.nodo_destino=nodo_destino
    

    @staticmethod
    def leer_csv(nombre_archivo):
        ident_carga = []
        peso = []
        nodo_origen = []
        nodo_destino = []
        
        with open(nombre_archivo, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            archivo.readline()
            for linea in lector_csv:
                ident_carga.append(linea[0])
                peso.append(linea[1])
                nodo_origen.append(linea[2])    
                nodo_destino.append(linea[3])
        return ident_carga, peso, nodo_origen, nodo_destino
    

class TramoItinerario:
    def __init__ (self, conexion:Conexion, vehiculo:Vehiculos, carga:float):
        self.conexion=conexion
        self.vehiculo=vehiculo
        self.carga=carga
    def calcular_tiempo(self):
        return self.conexion.distancia_km/self.vehiculo.velocidad
    def calcular_costo(self):
        cantidad_vehiculos= math.ceil(self.carga/self.vehiculo.capacidad)
        costo_x_vehiculo=(self.vehiculo.costo_fijo+self.vehiculo.costo_x_km*self.conexion.distancia_km+self.vehiculo.costo_x_kg*self.carga)
        return cantidad_vehiculos * costo_x_vehiculo

        
class Itinerario:
    def __init__(self, tramos: List[TramoItinerario], kpi: str):
        self.tramos = tramos
        self.kpi = kpi

    def tiempo_total(self):
        return sum(tramo.calcular_tiempo() for tramo in self.tramos)
    def costo_total(self):
        return sum(tramo.calcular_costo() for tramo in self.tramos)

    def __str___(self):
        texto='Resumen'
        for i in range(len(self.tramos)):
            texto+='Tramo' + str(i+1) + ':'+ str(self.tramos[i])+'\n'
        texto+='Tiempo total en horas: ' + str(self.tiempo_total())+'\n'
        texto+='Costo total: ' + str (self.costo_total())+'\n'
        texto+='KPI optimizado'+ self.kpi
        return texto


class Ferroviario(Vehiculos):
     def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
         super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)


class Maritimo(Vehiculos):
     def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
         super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)


class Automotor(Vehiculos):
     def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
         super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)


class Aereo(Vehiculos):
    def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
        super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)


