from Vehiculos import Vehiculos 

class Automotor(Vehiculos):
    """Vehículo automotor."""
    def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
        """Inicializa vehículo automotor."""
        super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)

