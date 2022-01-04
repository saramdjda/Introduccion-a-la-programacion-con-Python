class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}')

    # GETTERS y SETTERS
    # GET = Obtiene un valor, SET = Agrega un valor
    def get_precio(self):
        return self.precio


    def set_precio(self, precio):
        self.precio = precio

# Crear una clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca

    # Reescribir un método (debe llamarse igual)
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}, Alberca: {self.alberca}')
    
    # Agregar un método que sólo exista en Hotel
    def get_alberca(self):
        return self.alberca

hotel = Hotel('Hotel POO', '5 estrellas', 200, 'Sí')
hotel.mostrar_informacion()
alberca = hotel.get_alberca()
print(alberca)