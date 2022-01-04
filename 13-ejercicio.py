playlist = {} # Diccionario vacío
playlist['canciones'] = [] # Lista vacía de canciones

# Función principal
def app():
    # Agregar playlist
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('¿Cómo deseas nombrar la playlist?\r\n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            # Ya tenemos un nombre, desactivar el True
            agregar_playlist = False

            # Llamar la función para agregar canciones
            agregar_canciones()

def agregar_canciones():
    # Bandera para agregar canciones
    agregar_cancion = True

    while agregar_cancion:
        # Preguntar al usuario qupe canción desea agregar
        nombre_playlist = playlist['nombre']

        pregunta = f'Agrega canción a la playlist: {nombre_playlist}\r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones\r\n'

        cancion = input(pregunta)
        if cancion == 'X':
            # Dejar de agregar canciones
            agregar_cancion = False
            # Mostrar resumen de la playlist
            mostrar_resumen()
        else:
            # Agregar la canción a la playlist
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist}')
    print('Canciones:')
    for cancion in playlist['canciones']:
        print(cancion)

app()