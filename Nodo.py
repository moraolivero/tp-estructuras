from typing import List
from typing import Optional, Set


class Nodo:
    """Representa un nodo o punto de conexión en la red."""
    def __init__(self, nombre: str):
        """Inicializa un nodo con un nombre y lista de conexiones vacía."""
        if not isinstance(nombre, str) or not nombre:
            raise ValueError("El nombre del nodo debe ser una cadena no vacía.")
        self.nombre = nombre
        self.conexiones: Set["Conexion"] = set()

    def agregar_conexion(self, conexion: "Conexion"):
        """Agrega una conexión saliente al nodo."""
        self.conexiones.add(conexion)

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
    MODOS_VALIDOS = {'Ferroviaria', 'Aerea', 'Maritimo', 'Automotor', 'Fluvial'}
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
        if not isinstance(origen, Nodo) or not isinstance(destino, Nodo):
            raise ValueError("Origen y destino deben ser instancias de Nodo.")
        if not self.es_modo_valido(modo):
            raise ValueError(f"Modo de transporte inválido: {modo}. Debe ser uno de {self.MODOS_VALIDOS}.")
        if not isinstance(distancia_km, (int, float)) or distancia_km <=0:
            raise ValueError("La distancia debe ser un número positivo.")
        if restriccion is not None and not isinstance(restriccion, str):
            raise TypeError("La restricción debe ser una cadena o None.")
        
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
        
    def __eq__(self, other):
        """Define igualdad basada en los nodos origen y destino."""
        return (isinstance(other, Conexion) and 
                self.origen == other.origen and 
                self.destino == other.destino and 
                self.modo == other.modo and 
                self.distancia_km == other.distancia_km)
    def __hash__(self):
        """Permite usar la conexión en estructuras hash (sets, dicts)."""
        return hash((self.origen, self.destino, self.modo, self.distancia_km))
    @classmethod
    def es_modo_valido(cls, modo: str) -> bool:
        """Verifica si el modo de transporte es válido."""
        return modo in cls.MODOS_VALIDOS
    @classmethod
    def obtener_modos_validos(cls):
        'Devuelve los modos validos de trasnporte'
        return cls.MODOS_VALIDOS
    