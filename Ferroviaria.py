from Vehiculos import Vehiculos

class Ferroviaria(Vehiculos):
    """Vehículo ferroviario con costo especial según distancia."""
    def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
        """Inicializa vehículo ferroviario."""
        super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)
    def __str__(self):
        """Devuelve una representación en cadena del vehículo automotor."""
        return (f"Automotor(modo={self.modo}, velocidad={self.velocidad} km/h, "
                f"capacidad={self.capacidad} kg, costo fijo={self.costo_fijo}, "
                f"costo por km={self.costo_x_km}, costo por kg={self.costo_x_kg})")
    def calcular_costo_por_km(self, distancia: float) -> float:
        """Calcula costo por km, con tarifa fija si distancia >= 200 km."""
        if distancia >= 200:
            return 15  
        return self.costo_x_km 