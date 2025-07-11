from TramoItinerario import TramoItinerario
from typing import List
from TramoItinerario import TramoItinerario

class Itinerario:
    """Representa un itinerario completo formado por varios tramos."""
    KPI_VALIDOS = {'tiempo', 'costo'}
    def __init__(self, tramos: List[TramoItinerario], kpi: str):
        """Inicializa con la lista de tramos y el KPI a optimizar."""
        if not isinstance(tramos, list):
            raise TypeError("Los tramos deben ser una lista de TramoItinerario.")
        if not all(isinstance(tramo, TramoItinerario) for tramo in tramos):
            raise TypeError("Todos los tramos deben ser instancias de TramoItinerario.")
        if kpi not in self.KPI_VALIDOS:
            raise ValueError(f"KPI inválido. Debe ser uno de {self.KPI_VALIDOS}.")
        if not tramos:
            raise ValueError("La lista de tramos no puede estar vacía.")
        self.tramos = tramos
        self.kpi = kpi

    def tiempo_total(self):
        """Calcula el tiempo total del itinerario sumando todos los tramos."""
        return sum(tramo.calcular_tiempo() for tramo in self.tramos)

    def costo_total(self):
        """Calcula el costo total del itinerario sumando los tramos y peso."""
        costo_tramos = sum(tramo.calcular_costo_sin_kg() for tramo in self.tramos)
        if self.tramos:
            costo_x_kg = self.tramos[0].vehiculo.costo_x_kg * self.tramos[0].carga
        else:
            costo_x_kg = 0
        return costo_tramos + costo_x_kg

    def __str__(self):
        """Genera un resumen textual del itinerario."""
        texto = "Resumen\n"
        for i, tramo in enumerate(self.tramos):
            texto += f"  Tramo {i + 1}: {tramo.conexion}\n"
        texto += f"Tiempo total (horas): {self.tiempo_total():.2f}\n"
        texto += f"Costo total: ${self.costo_total():.2f}\n"
        texto += f"KPI optimizado: {self.kpi.upper()}\n"
        return texto
    