# Trabajo Práctico: Sistema de Transporte

## Descripción General

Este proyecto simula un sistema de transporte multimodal que permite planificar itinerarios óptimos para trasladar cargas a través de una red de nodos (ciudades) conectados por distintos medios (automotor, ferroviario, aéreo y marítimo). 

El sistema tiene como objetivo:
- Minimizar el costo total de transporte
- Minimizar el tiempo total de entrega

---

##  Principales Desafíos del Proyecto

### 1. Modelado de clases
- Diseñamos una estructura orientada a objetos para representar nodos, conexiones, vehículos, solicitudes, itinerarios y planificadores.

### 2. Implementación de restricciones

-El sistema contempla distintas restricciones operativas para que los itinerarios generados sean válidos y realistas. Estas restricciones se extraen del archivo de conexiones y se interpretan dinámicamente según el tipo de vehículo y el modo de transporte.

Peso Maximo: Si la carga excede el límite de peso de una conexión automotor, se descarta esa ruta.

Velocidad Maxima: En conexiones ferroviarias, el vehículo no puede superar la velocidad máxima permitida.

Probabilidad de mal clima: Ajusta la velocidad del avión según el riesgo climático (reducción porcentual). 


### 3. Costos variables y KPI
- Consideramos correctamente que el costo por kilogramo se aplica una sola vez en todo el itinerario, no en cada tramo.
- Implementamos la lógica para distribuir la carga entre múltiples vehículos si la capacidad individual no es suficiente.

### 4. Evitar loops
- Usamos una lista de nodos ya visitados para evitar ciclos en los itinerarios generados.

### 5. Visualizaciones
- Desarrollamos dos gráficos:
  - Distancia acumulada vs. tiempo acumulado
  - Costo acumulado vs. distancia acumulada

---

##  Estructura del Código

- `Nodo`: representa una ciudad o punto clave.
- `Conexion`: une dos nodos con un modo de transporte y una restricción.
- `Vehiculos`: clase base para distintos tipos de transporte (camión, tren, avión, barco).
- `TramoItinerario`: representa un tramo entre dos nodos usando un vehículo.
- `Itinerario`: agrupa todos los tramos de un recorrido y calcula tiempo y costo total.
- `SolicitudTransporte`: representa una solicitud de envío desde un origen a un destino con cierta carga.
- `Planificador`: busca los mejores itinerarios posibles según el KPI solicitado.
- `main()`: carga los archivos CSV, procesa todas las solicitudes y muestra resultados.

---

##  Archivos esperados

El sistema requiere 3 archivos CSV:

- nodos.csv: contiene los nombres de los nodos. Los modos disponibles se infieren desde las conexiones.
- conexiones.csv: columnas esperadas:
    `origen`, `destino`, `modo`, `distancia_km`, `restriccion`, `valor_restriccion`


- solicitudes.csv: columnas esperadas:
`id_carga`, `peso_carga`, `nodo_origen`, `nodo_destino`

- Para visualizar el codigo completo se tiene que correr el archivo `main.py` 
