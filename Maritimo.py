from Vehiculos import Vehiculos

class Maritimo(Vehiculos):
    """Vehículo marítimo."""
    def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
        """Inicializa vehículo marítimo."""
        super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)

