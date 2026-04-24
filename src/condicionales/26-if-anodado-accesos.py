# Se utiliza la estructura if-if para verificar si la contraseña es correcta.
usuario = 'admin'
contrasena = '1234'

if usuario == 'admin':
    if contrasena == '1234':
        print('Acceso concedido.')
    else:
        print('Contraseña incorrecta.')
else:
    print('Usuario no reconocido.')