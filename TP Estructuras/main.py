from tp1 import *

'''
nodo_junin = Nodo("Junin", {"Ferroviario", "Automotor", "Aereo"})
nodo_zarate = Nodo("Zarate", {"Ferroviario", "Automotor", "Maritimo"})


print("Printeo nodo Zarate: ")
print(nodo_zarate)
print(nodo_zarate.modos_disponibles)
print()

print("Printeo nodo Junin: ")
print(nodo_junin)
print(nodo_junin.modos_disponibles)
print()


print("Agrego esta conexion: ")
conexion_junin_a_zarate = Conexion(nodo_junin, nodo_zarate, "Automotor", 185)
nodo_junin.agregar_conexion(conexion_junin_a_zarate)

conexion1 = nodo_junin.conexiones[0]
print(conexion1)


print("Agrego la conexion opuesta: ")
conexion_zarate_a_junin = Conexion(nodo_zarate, nodo_junin, "Automotor", 185)
nodo_zarate.agregar_conexion(conexion_zarate_a_junin)

conexion1 = nodo_zarate.conexiones[0]
print(conexion1)
'''


# Crear nodos
zarate = Nodo("Zarate", {"Ferroviario", "Automotor", "Maritimo"})
buenos_aires = Nodo("Buenos Aires", {"Ferroviario", "Automotor", "Maritimo"})
mar_del_plata = Nodo("Mar del Plata", {"Ferroviario", "Automotor", "Maritimo"})

# Crear conexiones según pdf:
# Zárate → Buenos Aires: 85 km
c1 = Conexion(zarate, buenos_aires, "Ferroviario", 85, 100)
c1b = Conexion(zarate, buenos_aires, "Automotor", 85, 80)
c1c = Conexion(zarate, buenos_aires, "Maritimo", 85, 40)

# Buenos Aires → Mar del Plata: 384 km
c2 = Conexion(buenos_aires, mar_del_plata, "Ferroviario", 384, 100)
c2b = Conexion(buenos_aires, mar_del_plata, "Automotor", 384, 80)
c2c = Conexion(buenos_aires, mar_del_plata, "Maritimo", 384, 40)

# Agregar conexiones
zarate.agregar_conexion(c1); zarate.agregar_conexion(c1b); zarate.agregar_conexion(c1c)
buenos_aires.agregar_conexion(c2); buenos_aires.agregar_conexion(c2b); buenos_aires.agregar_conexion(c2c)


vehiculos = [
    Ferroviario("Ferroviario", velocidad=100, capacidad=150000, costo_fijo=100, costo_x_km=20, costo_x_kg=3),
    Automotor("Automotor", velocidad=80, capacidad=30000, costo_fijo=30, costo_x_km=5, costo_x_kg=1),
    Maritimo("Maritimo", velocidad=40, capacidad=100000, costo_fijo=500, costo_x_km=15, costo_x_kg=2),
]



planificador = Planificador(vehiculos)

# Solicitud: 70.000 kg desde Zárate hasta Mar del Plata
carga = 70000

# KPI: tiempo
it_tiempo = planificador.planificar_itinerario(zarate, mar_del_plata, carga, kpi="tiempo")
print("**Optimizando TIEMPO**:")
print(it_tiempo)

# KPI: costo
it_costo = planificador.planificar_itinerario(zarate, mar_del_plata, carga, kpi="costo")
print("**Optimizando COSTO**:")
print(it_costo)
