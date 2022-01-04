class Restaurant:

    def agregar_restaurant(self, nombre):
        self.nombre = nombre # Atributo
        print('Agregando...')

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')

# Instanciar la clase
restaurant_1 = Restaurant()
restaurant_1.agregar_restaurant('Pizzeria Don Pepe')
restaurant_1.mostrar_informacion()

restaurant_2 = Restaurant()
restaurant_2.agregar_restaurant('Hamburguesas Don Paco')
restaurant_2.mostrar_informacion()

# Mostrar la información
print(f'Nombre del restaurant: {restaurant_1.nombre}')
print(f'Nombre del restaurant: {restaurant_2.nombre}')