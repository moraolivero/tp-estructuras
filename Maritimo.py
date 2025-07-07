from Vehiculos import Vehiculos

class Maritimo(Vehiculos):
    """Vehículo marítimo."""
    def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
        """Inicializa vehículo marítimo."""
        super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)
    def calcular_costo_total(self, distancia_km: float, carga_kg: float, cantidad_vehiculos: int) -> float:
        suplemento_portuario = 1000
        base = super().calcular_costo_total(distancia_km, carga_kg, cantidad_vehiculos)
        return base + suplemento_portuario
    def __str__(self):
        """Devuelve una representación en cadena del vehículo marítimo."""
        return (f"Maritimo(modo={self.modo}, velocidad={self.velocidad} km/h, "
                f"capacidad={self.capacidad} kg, costo fijo={self.costo_fijo}, "
                f"costo por km={self.costo_x_km}, costo por kg={self.costo_x_kg})")
