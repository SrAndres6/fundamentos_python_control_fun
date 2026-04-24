# Se utiliza la estructura if-if para verificar si la edad y el estado civil son correctos.
edad = 30
estado_civil = 'soltero'

if edad >= 18:
    if estado_civil == 'casado':
        print('Eres un adulto casado.')
    else:
        print('Eres un adulto soltero.')
else:
    print('Eres menor de edad.')