nombre = input('¿Cuál es tu nombre?\r\n')

print(f'Hola, {nombre}')

# Leer datos que serás números
edad = input('¿Cuál es tu edad?\r\n')
# Convertar edad string a entero
edad = int(edad)

if edad >= 18:
    print('Ya puedes votar')
else:
    print('Aún no puedes votar')

# Mezclarlo con operadores
numero = input('Agrega un número y te diré si es par o impar\r\n')
numero = int(numero)

if numero % 2 == 0:
    print(f'El número {numero} es par')
else:
    print(f'El número {numero} es impar')