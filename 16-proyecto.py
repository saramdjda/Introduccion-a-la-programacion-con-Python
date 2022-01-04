# Aplicación de directorio o agenda de contactos

import os

CARPETA = 'contactos/' # Carpeta de Contactos
EXTENSION = '.txt' # Extensión de los archivos

# Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

# App
def app():
    # Revisa si la carpeta existe o no
    crear_directorio()

    # Muestra el menú de opciones
    mostrar_menu()

    # Preguntar al usuario la acción a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        # Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar == False
        elif opcion == 4:
            buscar_contacto()
            preguntar == False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        elif opcion == 6:
            print('\r\n ¡Hasta luego! \r\n')
            exit()
        else:
            print('\r\nOpción no válida, intente de nuevo\r\n')
            mostrar_menu()

# Menú de opciones
def mostrar_menu():
    print('Menú:')
    print('1) Agregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver todos los contactos')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')
    print('6) Salir')

# Crear carpeta o directorio
def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crear la carpeta
        os.makedirs(CARPETA)

# Funciones del menú

# Revisar si el archivo ya existe
def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

# Agregar nuevo contacto
def agregar_contacto():
    print('* Agregar nuevo contacto *\r\n')
    nombre_contacto = input('Nombre: \r\n')

    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)

    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            # Resto de los campos
            telefono_contacto = input('Telefono: \r\n')
            categoria_contacto = input('Categoria: \r\n')

            # Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\n')
            archivo.write('Telefono: ' + contacto.telefono + '\n')
            archivo.write('Categoria: ' + contacto.categoria + '\n')

            # Mostrar un mensaje de éxito
            print('\r\n ¡Contacto agregado correctamente! \r\n')
    else:
        print('\r\n Ese contacto ya existe \r\n')
    
    # Reiniciar la app
    app()

# Editar contacto
def editar_contacto():
    print('* Editar contacto *\r\n')
    nombre_anterior = input('Nombre: \r\n')

    # Revisar si el archivo ya existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        # Abrir el archivo
        archivo = open(CARPETA + nombre_anterior + EXTENSION, 'w')
        
        # Resto de los campos
        nombre_contacto = input('Nombre: \r\n')
        telefono_contacto = input('Telefono: \r\n')
        categoria_contacto = input('Categoria: \r\n')

        # Instanciar la clase
        contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

        # Escribir en el archivo
        archivo.write('Nombre: ' + contacto.nombre + '\n')
        archivo.write('Telefono: ' + contacto.telefono + '\n')
        archivo.write('Categoria: ' + contacto.categoria + '\n')

        # Cerrar el archivo
        archivo.close()

        # Renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

        # Mostrar un mensaje de éxito
        print('\r\n ¡Contacto editado correctamente! \r\n')
    else:
        print('\r\n Ese contacto no existe \r\n')

    # Reiniciar la app
    app()

# Ver todos los contactos
def mostrar_contactos():
    print('* Ver todos los contactos *\r\n')
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                # Imprime los contenidos
                print(linea.rstrip())
            # Imprime un separador entre los contactos
            print('\n---\n')

# Buscar contacto
def buscar_contacto():
    print('* Buscar contacto *\r\n')
    nombre = input('Nombre: \r\n')

    # Revisar si el archivo ya existe antes de editarlo
    existe = existe_contacto(nombre)

    if existe:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Información del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    else:
        print('\r\n Ese contacto no existe \r\n')

    # Reiniciar la app
    app()

# Eliminar contacto
def eliminar_contacto():
    print('* Eliminar contacto *\r\n')
    nombre = input('Nombre: \r\n')

    # Revisar si el archivo ya existe antes de editarlo
    existe = existe_contacto(nombre)

    if existe:
        os.remove(CARPETA + nombre + EXTENSION)

        # Mostrar un mensaje de éxito
        print('\r\n ¡Contacto eliminado correctamente! \r\n')
    else:
        print('\r\n Ese contacto no existe \r\n')

    # Reiniciar la app
    app()

app()