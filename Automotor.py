from Vehiculos import Vehiculos 
from typing import Optional
class Automotor(Vehiculos):
    """Vehículo automotor."""
    def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
        """Inicializa vehículo automotor."""
        super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)
    def calcular_tiempo(self, distancia_km: float, limite_legal: Optional[float] = None) -> float:
        velocidad = self.velocidad
        if limite_legal is not None:
            velocidad = min(velocidad, limite_legal)
        return distancia_km / velocidad
    def __str__(self):
        """Devuelve una representación en cadena del vehículo automotor."""
        return (f"Automotor(modo={self.modo}, velocidad={self.velocidad} km/h, "
                f"capacidad={self.capacidad} kg, costo fijo={self.costo_fijo}, "
                f"costo por km={self.costo_x_km}, costo por kg={self.costo_x_kg})")