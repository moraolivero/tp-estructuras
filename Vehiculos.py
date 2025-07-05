


class Vehiculos:
    """Clase base para vehículos con características y costos."""
    tipo_vehiculo = ["Ferroviaria", "Maritimo", "Automotor", "Aerea"]

    def __init__(
        self,
        modo: str,
        velocidad: int,
        capacidad: int,
        costo_fijo: float,
        costo_x_km: float,
        costo_x_kg: float,
    ):
        """Inicializa un vehículo con sus atributos principales."""
        self.modo = modo
        self.velocidad = velocidad
        self.capacidad = capacidad
        self.costo_fijo = costo_fijo
        self.costo_x_km = costo_x_km
        self.costo_x_kg = costo_x_kg

    def calcular_costo_por_km (self, distancia):
        """Calcula costo por km (puede ser sobrescrito en subclases)."""
        return self.costo_x_km 

    def validar_int(dato):
        """Valida que un dato sea entero."""
        try:
            dato = int(dato)
        except TypeError:
            raise TypeError("El dato ingresado no es un numero entero")

    def validar_float(dato):
        """Valida que un dato sea float."""
        try:
            dato = float(dato)
        except TypeError:
            raise TypeError("El dato ingresado no es un numero valido")

    @classmethod
    def validar_modo(cls, modo: str):
        """Verifica que el modo esté entre los tipos válidos."""
        return modo in cls.tipo_vehiculo
