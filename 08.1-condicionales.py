# Revisar si una condición es mayor a
balance = 0
if balance > 0:
    print('Puedes pagar')
else:
    print('No tienes saldo')

# Likes
likes = 200
if likes >= 200:
    print('Excelente, ¡200 likes!')
else:
    print('Casi llegas a los 200 likes')

# If con texto
lenguaje = 'PHP'
if not lenguaje == 'Python':
    print('Excelente decisión')

# Evaluar un booleano
usuario_autenticado = True

if usuario_autenticado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesión')

# Evaluar un elemento d una lista
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript', 'PHP', 'Ruby']

if 'PHP' in lenguajes:
    print('PHP sí existe')
else:
    print('No, no está en la lista')

# If anidados
usuario_autenticado = True
usuario_admin = True

if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sesión')