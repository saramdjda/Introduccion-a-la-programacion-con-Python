def app():
    # Crear el archivo
    archivo = open('archivo.txt', 'w') # W es escritura, si no existe lo creará

    # Generar números en archivo
    for i in range  (0, 20):
        archivo.write('Esta es la linea ' + str(i) + '\n')

    # Cerrar el archivo
    archivo.close()

app()