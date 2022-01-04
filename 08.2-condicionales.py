# Ejemplo con elif
ocupacion = 'Estudiante'

if ocupacion == 'Estudiante':
    print('Tienes 50% de descuento')
elif ocupacion == 'Jubliado':
    print('Tienes 75% de descuento')
elif ocupacion == 'Desempleado':
    print('Tienes 10% de descuento')
else:
    print('Debes pagar el 100%')