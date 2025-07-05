from typing import List
from typing import Optional

class Nodo:
    """Representa un nodo o punto de conexión en la red."""
    def __init__(self, nombre: str):
        """Inicializa un nodo con un nombre y lista de conexiones vacía."""
        self.nombre = nombre
        self.conexiones: List["Conexion"] = []

    def agregar_conexion(self, conexion: "Conexion"):
        """Agrega una conexión saliente al nodo."""
        self.conexiones.append(conexion)

    def __str__(self):
        """Retorna el nombre del nodo."""
        return self.nombre
    
    def __eq__(self, other):
        """Define igualdad basada en el nombre del nodo."""
        return isinstance (other, Nodo) and  self.nombre == other.nombre

    def __hash__ (self):
        """Permite usar el nodo en estructuras hash (sets, dicts)."""
        return hash (self.nombre)
    

class Conexion:
    """Representa una conexión entre dos nodos con modo, distancia y restricciones."""
    def __init__(
        self,
        origen: Nodo,
        destino: Nodo,
        modo: str,
        distancia_km: float,
        restriccion: Optional[str],
        valor_restriccion: Optional[float]
        ):
        """Inicializa una conexión con sus atributos."""
        self.origen = origen
        self.destino = destino
        self.modo = modo
        self.distancia_km = distancia_km
        self.restriccion = restriccion
        self.valor_restriccion = valor_restriccion

    def __str__(self):
        """Representación en texto de la conexión."""
        return f"{self.origen}  -> {self.destino} ({self.modo}, {self.distancia_km} km)"

    def validar_carga (self, valor: float) -> bool:
        """Valida si el valor cumple con la restricción de la conexión."""
        if self.restriccion == "peso maximo":
            return valor <= self.valor_restriccion
        return True
    
    def validar_modo(self, modo: str) -> bool:
        """Valida si el modo de transporte es compatible con la conexión."""
        return modo is None or self.modo == modo 