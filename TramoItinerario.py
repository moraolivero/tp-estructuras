

import math
from Nodo import Conexion
from Vehiculos import Vehiculos
from Ferroviaria import Ferroviaria

class TramoItinerario:
    """Representa un tramo de un itinerario con conexión, vehículo y carga."""
    def __init__(self, conexion: Conexion, vehiculo: Vehiculos, carga: float):
        """Inicializa el tramo con conexión, vehículo y peso de carga."""
        if not isinstance(conexion, Conexion):
            raise TypeError("La conexión debe ser una instancia de Conexion.")
        if not isinstance(vehiculo, Vehiculos):
            raise TypeError("El vehículo debe ser una instancia de Vehiculos.")
        if not isinstance(carga, (int, float)) or carga <= 0:
            raise ValueError("La carga debe ser un número positivo.")
        self.conexion = conexion
        self.vehiculo = vehiculo
        self.carga = carga
        

    def calcular_tiempo(self):
        restriccion = self.conexion.valor_restriccion if self.conexion.restriccion in ["velocidad_maxima", "probabilidad_mal_clima"] else None
        return self.vehiculo.calcular_tiempo(self.conexion.distancia_km, restriccion)

    def calcular_costo_sin_kg(self):
        cantidad_vehiculos = math.ceil(self.carga / self.vehiculo.capacidad)
        return cantidad_vehiculos * (self.vehiculo.obtener_costo_fijo() + self.vehiculo.calcular_costo_por_km(self.conexion.distancia_km) * self.conexion.distancia_km)

    def calcular_costo(self):
        cantidad_vehiculos = math.ceil(self.carga / self.vehiculo.capacidad)
        return self.vehiculo.calcular_costo_total(self.conexion.distancia_km, self.carga, cantidad_vehiculos)

