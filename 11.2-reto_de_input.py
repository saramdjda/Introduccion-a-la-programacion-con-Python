# Examen simple de 3 preguntas
nota = 0

print('* Examen final de biología *')
print('El examen consta de 3 preguntas')
print('Por favor responda con "SI" o "NO" a cada una de ellas')

# Pregunta 1 (respuesta correcta: 'NO')
pregunta_1 = input('¿Existen animales autótrofos\r\n')
if pregunta_1 == 'NO':
    nota += 1

# Pregunta 2 (respuesta correcta: 'SI')
pregunta_2 = input('¿La flor es un órgano reproductor de las plantas?\r\n')
if pregunta_2 == 'SI':
    nota += 1

# Pregunta 3 (respuesta correcta: 'NO')
pregunta_3 = input('¿EL koala es un oso?\r\n')
if pregunta_3 == 'NO':
    nota += 1

if nota == 0:
    print(f'Tu calificación es {nota} de 3 puntos. Tu resultado es MALO.')
elif nota == 1:
    print(f'Tu calificación es {nota} de 3 puntos. Tu resultado es REGULAR.')
elif nota == 2:
    print(f'Tu calificación es {nota} de 3 puntos. Tu resultado es BUENO.')
else:
    print(f'Tu calificación es {nota} de 3 puntos. Tu resultado es EXCELENTE.')