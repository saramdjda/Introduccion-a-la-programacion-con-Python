# Iniciar un diccionario vacío
jugador = {}
print(jugador)

# Se une un jugador
jugador['nombre'] = 'Sara'
jugador['puntaje'] = 0
print(jugador)

# Incrementando el puntaje
jugador['puntaje'] = 100
print(jugador)

# Acceder a un valor
print(jugador.get('consola', 'No existe ese valor'))

# Iterar en el diccionario
for llave, valor in jugador.items():
    print(llave)
    print(valor)

# Eliminar jugador y puntaje
del jugador['nombre']
del jugador['puntaje']