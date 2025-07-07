from typing import Optional

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
        if not self.validar_modo(modo):
            raise ValueError(f"Modo de transporte inválido. Debe ser uno de: {self.tipo_vehiculo}")
        """Inicializa un vehículo con sus atributos principales."""
        if not isinstance (modo, str):
            raise TypeError("El modo debe ser una cadena de texto.")
        self.validar_int(velocidad, "velocidad")
        self.validar_int(capacidad, "capacidad")
        self.validar_float(costo_fijo, "costo_fijo")
        self.validar_float(costo_x_km, "costo_x_km")
        self.validar_float(costo_x_kg, "costo_x_kg")
        self.modo = modo
        self.velocidad = velocidad
        self.capacidad = capacidad
        self.costo_fijo = costo_fijo
        self.costo_x_km = costo_x_km
        self.costo_x_kg = costo_x_kg

    

    def calcular_costo_por_km (self, distancia):
        """Calcula costo por km (puede ser sobrescrito en subclases)."""
        return self.costo_x_km 

    def calcular_tiempo(self, distancia_km:float, restriccion: Optional[float] = None) -> float:
        """Calcula el tiempo necesario para recorrer una distancia dada."""
        return distancia_km / self.velocidad if restriccion is None else distancia_km / min(self.velocidad, restriccion)
    
    def calcular_costo_total(self, distancia_km: float, carga_kg: float, cantidad_vehiculos: int) -> float:
        costo_tramo = cantidad_vehiculos * (self.costo_fijo + self.costo_x_km * distancia_km)
        costo_kg = self.costo_x_kg * carga_kg
        return costo_tramo + costo_kg
        
    def obtener_costo_fijo(self):
        """Obtiene el costo fijo del vehículo."""
        return self.costo_fijo

    @classmethod
    def validar_modo(cls, modo: str):
        """Verifica que el modo esté entre los tipos válidos."""
        return modo in cls.tipo_vehiculo
    @staticmethod
    def validar_int(dato, nombre_campo='dato'):

        '''Valida que un dato sea entero.'''
        if not isinstance(dato, int):
            raise TypeError("El dato ingresado no es un numero entero")
    @staticmethod
    def validar_float(dato, nombre_campo='dato'):
        '''Valida que un dato sea float.'''
        if not isinstance(dato, (int, float)):
            raise TypeError("El dato ingresado no es un numero valido")
    
    def obtener_detalle(self) -> str:
        return (f"{self.__class__.__name__}(modo={self.modo}, velocidad={self.velocidad} km/h, "
                f"capacidad={self.capacidad} kg, costo fijo={self.costo_fijo}, "
                f"costo por km={self.costo_x_km}, costo por kg={self.costo_x_kg})")

    def __str__(self):
        return self.obtener_detalle()

