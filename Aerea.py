from Vehiculos import Vehiculos
from typing import Optional

class Aerea(Vehiculos):
    """Vehículo aéreo."""
    def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
        """Inicializa vehículo aéreo."""
        super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)

    def calcular_tiempo (self, distancia_km: float, probabilidad_mal_clima: Optional[float]=None)-> float:
        velocidad= self.velocidad
        if probabilidad_mal_clima:
            velocidad *= (1 - probabilidad_mal_clima)
        return distancia_km / velocidad
        