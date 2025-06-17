import csv
import math
from typing import List, Dict, Set, Optional
import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.conexiones: List["Conexion"] = []

    def agregar_conexion(self, conexion: "Conexion"):
        self.conexiones.append(conexion)

    def __str__(self):
        return self.nombre
    
    def __eq__(self, other):
        return isinstance (other, Nodo) and  self.nombre == other.nombre

    def __hash__ (self):
        return hash (self.nombre)
    

class Conexion:
    def __init__(
        self,
        origen: Nodo,
        destino: Nodo,
        modo: str,
        distancia_km: float,
        restriccion: Optional[str],
        valor_restriccion: Optional[float]
        ):
        self.origen = origen
        self.destino = destino
        self.modo = modo
        self.distancia_km = distancia_km
        self.restriccion = restriccion
        self.valor_restriccion = valor_restriccion

    def __str__(self):
        return f"{self.origen}  -> {self.destino} ({self.modo}, {self.distancia_km} km)"


class Vehiculos:
    tipo_vehiculo = ["Ferroviario", "Maritimo", "Automotor", "Aereo"]

    def __init__(
        self,
        modo: str,
        velocidad: int,
        capacidad: int,
        costo_fijo: float,
        costo_x_km: float,
        costo_x_kg: float,
    ):
        self.modo = modo
        self.velocidad = velocidad
        self.capacidad = capacidad
        self.costo_fijo = costo_fijo
        self.costo_x_km = costo_x_km
        self.costo_x_kg = costo_x_kg

    def validar_int(dato):
        try:
            dato = int(dato)
        except TypeError:
            raise TypeError("El dato ingresado no es un numero entero")

    def validar_float(dato):
        try:
            dato = float(dato)
        except TypeError:
            raise TypeError("El dato ingresado no es un numero valido")

    @classmethod
    def validar_modo(cls, modo: str):
        return modo in cls.tipo_vehiculo

class Planificador:
    def __init__(self, vehiculos: List[Vehiculos]):
        self.vehiculos = vehiculos

    def buscar_mejor_itinerario(
        self,
        nodo_actual: Nodo,
        nodo_destino: Nodo,
        carga: float,
        kpi: str,
        visitados: List[Nodo],
        tramos_actuales: List["TramoItinerario"],
    ) -> Optional["Itinerario"]:

        if nodo_actual == nodo_destino:
            return Itinerario(tramos_actuales, kpi)

        visitados.append(nodo_actual)
        mejores_itinerarios = []

        for conexion in nodo_actual.conexiones:
            if conexion.restriccion == "peso maximo"  and carga > conexion.valor_restriccion:
                continue

            siguiente_nodo = conexion.destino
            if siguiente_nodo in visitados:
                continue

            vehiculos_compatibles = [
                v for v in self.vehiculos if v.modo == conexion.modo
            ]

            for vehiculo in vehiculos_compatibles:
                tramo = TramoItinerario(conexion, vehiculo, carga)
                nuevo_tramo = tramos_actuales + [tramo]

                itinerario = self.buscar_mejor_itinerario(
                    siguiente_nodo, nodo_destino, carga, kpi, visitados.copy(), nuevo_tramo
                )

                if itinerario:
                    mejores_itinerarios.append(itinerario)

        if not mejores_itinerarios:
            return None

        if kpi == "tiempo":
            return min(mejores_itinerarios, key=lambda i: i.tiempo_total())
        elif kpi == "costo":
            return min(mejores_itinerarios, key=lambda i: i.costo_total())
        else:
            raise ValueError("KPI inválido. Debe ser 'tiempo' o 'costo'.")


    def planificar_itinerario(
        self,
        nodo_origen: Nodo,
        nodo_destino: Nodo,
        carga: float,
        kpi: str
    ) -> Optional["Itinerario"]:
        return self.buscar_mejor_itinerario(
            nodo_origen,
            nodo_destino,
            carga,
            kpi,
            visitados=[],
            tramos_actuales=[],
        )


class SolicitudTransporte:
    def __init__(
        self,
        identificacion_carga: str,
        peso_carga: float,
        nodo_origen: Nodo,
        nodo_destino: Nodo,
    ):
        self.identificacion_carga = identificacion_carga
        self.peso_carga = peso_carga
        self.nodo_origen = nodo_origen
        self.nodo_destino = nodo_destino

    @staticmethod
    def leer_csv(nombre_archivo: str, nodos: Dict[str, Nodo])->List['SolicitudTransporte']:
        solicitudes=[] 
        with open (nombre_archivo, newline='') as archivo: 
            lector= csv.reader (archivo)
            next(lector)
            for linea in lector: 
                ident= linea[0]
                peso= float(linea[1])
                origen=nodos.get(linea[2])
                destino= nodos.get(linea[3])
                if origen is None or destino is None:
                    raise ValueError (f'Nodo invalido')
                solicitud=SolicitudTransporte(ident, peso, origen, destino)
                solicitudes.append(solicitud)
        return solicitudes 


class TramoItinerario:
    def __init__(self, conexion: Conexion, vehiculo: Vehiculos, carga: float):
        self.conexion = conexion
        self.vehiculo = vehiculo
        self.carga = carga

    def calcular_tiempo(self):
        if self.conexion.restriccion == "velocidad_maxima":
            velocidad = min(self.vehiculo.velocidad, self.conexion.valor_restriccion)
        elif self.vehiculo.modo == "Aereo" and self.conexion.restriccion == "probabilidad_mal_clima":
            velocidad = self.vehiculo.velocidad * (1 - self.conexion.valor_restriccion)
        else:
            velocidad = self.vehiculo.velocidad
        return self.conexion.distancia_km / velocidad

    def calcular_costo_sin_kg(self):
        cantidad_vehiculos = math.ceil(self.carga / self.vehiculo.capacidad)
        return cantidad_vehiculos * (
            self.vehiculo.costo_fijo + self.vehiculo.costo_x_km * self.conexion.distancia_km
        )
    
    def calcular_costo(self):
        return self.calcular_costo_sin_kg() 

class Itinerario:
    def __init__(self, tramos: List[TramoItinerario], kpi: str):
        self.tramos = tramos
        self.kpi = kpi

    def tiempo_total(self):
        return sum(tramo.calcular_tiempo() for tramo in self.tramos)

    def costo_total(self):
        costo_tramos = sum(tramo.calcular_costo_sin_kg() for tramo in self.tramos)
        if self.tramos:
            costo_x_kg = self.tramoa[0].vehiculo.costo_x_kg * self.tramos[0].carga
        else:
            costo_x_kg = 0
        return costo_tramos + costo_x_kg

    def __str__(self):
        texto = "Resumen\n"
        for i, tramo in enumerate(self.tramos):
            texto += f"  Tramo {i + 1}: {tramo.conexion}\n"
        texto += f"Tiempo total (horas): {self.tiempo_total():.2f}\n"
        texto += f"Costo total: ${self.costo_total():.2f}\n"
        texto += f"KPI optimizado: {self.kpi.upper()}\n"
        return texto


class Ferroviario(Vehiculos):
    def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
        super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)
    def calcular_costo_por_km(self, distancia_km: float) -> float:
        if distancia_km > 300:
            return 15  
        return self.costo_x_km


class Maritimo(Vehiculos):
    def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
        super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)


class Automotor(Vehiculos):
    def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
        super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)


class Aereo(Vehiculos):
    def __init__(self, modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg):
        super().__init__(modo, velocidad, capacidad, costo_fijo, costo_x_km, costo_x_kg)


def cargar_nodos_desde_csv(ruta:str)-> Dict[str, Nodo]:
    nodos={}
    with open(ruta, newline='') as archivo:
        lector=csv.reader(archivo)
        next(lector)
        for nombre, _ in lector:
            nodos[nombre]= Nodo(nombre)
    return nodos

def cargar_conexiones_desde_csv(ruta:str, nodos: Dict[str, Nodo]) -> None:
    with open(ruta, newline='') as archivo:
        lector=csv.reader(archivo)
        next(lector)
        for linea in lector:
            origen, destino, modo, distancia, restriccion, valor=linea
            if origen not in nodos or destino not in nodos:
                raise ValueError(f'Origen o destino no encontrado en nodos:{linea}')
            conexion=Conexion(origen=nodos[origen],
                              destino=nodos[destino],
                              modo=modo ,
                              distancia_km=float(distancia),
                              restriccion=restriccion if restriccion else None,
                valor_restriccion=float(valor) if valor else None
            )
            nodos[origen].agregar_conexion(conexion)




def graficar_distancia_vs_tiempo(itinerario: Itinerario):
    distancias = []
    tiempos = []
    tiempo_acumulado = 0
    distancia_acumulada = 0
    for tramo in itinerario.tramos:
        distancia_acumulada += tramo.conexion.distancia_km
        tiempo_acumulado += tramo.calcular_tiempo()
        distancias.append(distancia_acumulada)
        tiempos.append(tiempo_acumulado)

    plt.plot(tiempos, distancias, marker='o')
    plt.xlabel("Tiempo acumulado (horas)")
    plt.ylabel("Distancia acumulada (km)")
    plt.title("Distancia vs. Tiempo")
    plt.grid(True)
    plt.show()

def graficar_costo_vs_distancia(itinerario: Itinerario):
    distancias = []
    costos = []
    costo_acumulado = 0
    distancia_acumulada = 0
    for tramo in itinerario.tramos:
        distancia_acumulada += tramo.conexion.distancia_km
        costo_acumulado += tramo.calcular_costo_sin_kg()
        distancias.append(distancia_acumulada)
        costos.append(costo_acumulado)

    plt.plot(distancias, costos, marker='o')
    plt.xlabel("Distancia acumulada (km)")
    plt.ylabel("Costo acumulado ($)")
    plt.title("Costo vs. Distancia")
    plt.grid(True)
    plt.show()



"""ejemplo de recorrido de grafo
Tener el tiempo minimo de todas los caminos posibles

Yo voy a recorrer nodo por nodo:  (for loop)
 - Junin
 - Zarate
 - Azul
 - Mar del plata
  
  localidades_ya_visitadas = []
  localidades_ya_visitadas.append(Junin)

  para cada uno de estos nodos, me voy a fijar las conexiones:  (for loop)
  Junin -- Conexiones -- [Zarate, Buenos Aires, Azul]

    - Entro en Zarate, y me fijo las conexiones de Zarate que no esten en localidades_ya_visitadas
        [ Buenos Aires ]
            - Entro en Buenos Aires: 
  





Tener el tiempo minimo entre 2 localidades


lista_de_caminos = [camino1, camino2]
lista_de_tiempos = [tiempo1, tiempo2]
lista_de_costos =  [costo1, costo2]

LOCALIDAD_DE_ORIGEN = Junin
LOCALIDAD_DE_DESTINO = Mar del plata

localidades_ya_visitadas = []
localidades_ya_visitadas.append(LOCALIDAD_DE_ORIGEN)


Junin -- Conexiones -- [Zarate, Buenos Aires, Azul]
- Entro en Zarate, y me fijo las conexiones de Zarate que no esten en localidades_ya_visitadas
    [ Buenos Aires ]
        - Entro en Buenos Aires: 
        .
        .
        .
        Hasta que 
            Caso 1) Ya no me queden conexiones que no esten en localidades_ya_visitadas y que el nodo en el que me encuentro
            sea el nodo LOCALIDAD_DE_DESTINO  ---> Voy a agregar este camino, con su tiempo y costo total respectivos a las listas
            Caso 2) Ya no me queden conexiones que no esten en localidades_ya_visitadas y que el nodo en el que me encuentro no sea
            el nodo LOCALIDAD_DE_DESTINO --> en este caso no hago nada, vuelvo en la recursion
 

def visitar_hijos(nodo, ya_visitados):
    if len(nodo.conexiones) == 0:
        return
    for conexion in nodo.conexiones:
        destino = conexion.destino
        if not destino in ya_visitados:
            visitar_hijos(destino, ya_visitados + [nodo])

        
visitar_hijos(Junin, []):
                
    Junin.conexiones [Junin-Zarate, Junin-Azul, Junin-Buenos Aires] --> 3

    for conexion in [Junin-Zarate, Junin-Azul, Junin-Buenos Aires]:
        conexion = Junin-Zarate
        destino = Zarate
        visitar_hijos(Zarate, [Junin])

visitar_hijos(Zarate, [Junin]):
    Zarate.conexiones [Zarate-Junin, Zarate-Buenos Aires] --> 2

    for conexion in [Zarate-Junin, Zarate-Buenos Aires]:
        Iteracion 1:
            conexion = Zarate-Junin
            destino = Junin
            if not Junin in [Junin]:
                --- no se ejecuta
        Iteracion 2:
            conexion = Zarate-Buenos Aires
            destino = Buenos Aires
            if not Buenos Aires in [Junin]:
                visitar_hijos(Buenos Aires, [Junin, Buenos Aires])
"""