lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

print(lenguajes)

# Los arrays (listas) comienzan en la posición 0
print(lenguajes[0]) # Python

# Ordenar los elementos
lenguajes.sort()
print(lenguajes)

# Acceder a un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

# Modificando valores de un arreglo
lenguajes[2] = 'PHP'
print(lenguajes)

# Agregar elemento a un arreglo
lenguajes.append('Ruby')
print(lenguajes)

# Eliminar elementos de un arreglo
del lenguajes [1]
print(lenguajes)

# Eliminar el último elemento de un arreglo
lenguajes.pop()
print(lenguajes)

# Eliminar con pop una pisición en específico
lenguajes.pop(0)
print(lenguajes)

# Eliminar por nombre
lenguajes.remove('PHP')
print(lenguajes)