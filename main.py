from tp1 import Nodo, Conexion


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
