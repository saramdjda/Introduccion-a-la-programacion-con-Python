class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.__precio = precio # Default Public, PROTECTED, PRIVATE

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.__precio}')

    # GETTERS y SETTERS
    # GET = Obtiene un valor, SET = Agrega un valor
    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

# Instanciar la clase
restaurant_1 = Restaurant('Pizzeria Don Pepe', 'comida casual', 50)
restaurant_1.mostrar_informacion()
restaurant_1.set_precio(70)
precio_1 = restaurant_1.get_precio()
print(precio_1)

restaurant_2 = Restaurant('Hamburguesas Don Paco', 'comida rápida', 20)
restaurant_2.mostrar_informacion()
restaurant_2.set_precio(40)
precio_2 = restaurant_2.get_precio()
print(precio_2)