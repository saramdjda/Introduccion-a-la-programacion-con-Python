class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}')

# Instanciar la clase
restaurant_1 = Restaurant('Pizzeria Don Pepe', 'comida casual', 50)
restaurant_1.mostrar_informacion()

restaurant_2 = Restaurant('Hamburguesas Don Paco', 'comida rápida', 20)
restaurant_2.mostrar_informacion()