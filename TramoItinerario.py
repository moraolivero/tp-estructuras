

import math
from Nodo import Conexion
from Vehiculos import Vehiculos
from Ferroviaria import Ferroviaria

class TramoItinerario:
    """Representa un tramo de un itinerario con conexión, vehículo y carga."""
    def __init__(self, conexion: Conexion, vehiculo: Vehiculos, carga: float):
        """Inicializa el tramo con conexión, vehículo y peso de carga."""
        self.conexion = conexion
        self.vehiculo = vehiculo
        self.carga = carga

    def calcular_tiempo(self):
        """Calcula el tiempo necesario para completar el tramo."""
        if self.conexion.restriccion == "velocidad_maxima":
            velocidad = min(self.vehiculo.velocidad, self.conexion.valor_restriccion)
        elif self.vehiculo.modo == "Aerea" and self.conexion.restriccion == "probabilidad_mal_clima":
            velocidad = self.vehiculo.velocidad * (1 - self.conexion.valor_restriccion)
        else:
            velocidad = self.vehiculo.velocidad
        return self.conexion.distancia_km / velocidad

    def calcular_costo_sin_kg(self):
        """Calcula el costo del tramo sin considerar el peso de la carga."""
        cantidad_vehiculos = math.ceil(self.carga / self.vehiculo.capacidad)

        if isinstance(self.vehiculo, Ferroviaria):
            costo_km = self.vehiculo.calcular_costo_por_km(self.conexion.distancia_km)
        else:
            costo_km = self.vehiculo.costo_x_km

        return cantidad_vehiculos * (
            self.vehiculo.costo_fijo + costo_km * self.conexion.distancia_km
        )

    def calcular_costo(self):
        """Calcula el costo total del tramo, incluyendo carga y tipo de vehículo."""
        cantidad_vehiculos = math.ceil(self.carga / self.vehiculo.capacidad)
    
        if self.vehiculo.modo == "Fluvial":
            costo_fijo = 500
        elif self.vehiculo.modo == "Maritimo":
            costo_fijo = 1500
        else:
            costo_fijo = self.vehiculo.costo_fijo

        if isinstance(self.vehiculo, Ferroviaria):
            costo_km = self.vehiculo.calcular_costo_por_km(self.conexion.distancia_km)
        else:
            costo_km = self.vehiculo.costo_x_km

        costo_fijo_km = cantidad_vehiculos * (costo_fijo + costo_km * self.conexion.distancia_km)
        costo_kg = self.vehiculo.costo_x_kg * self.carga

        return costo_fijo_km + costo_kg
 