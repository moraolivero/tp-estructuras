from Vehiculos import Vehiculos

class Aerea(Vehiculos):
    """Vehículo aéreo."""
    def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
        """Inicializa vehículo aéreo."""
        super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)