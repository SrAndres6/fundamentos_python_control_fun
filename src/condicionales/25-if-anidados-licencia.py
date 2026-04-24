# Se utiliza la estructura if-if para verificar si la edad y el estado civil son correctos.
edad = 16
permiso_padres = True

if edad >= 18:
    print('Puedes obtener la licencia de conducir.')
elif edad >= 16 and permiso_padres:
    print('Puedes obtener la licencia con permiso de tus padres.')
elif edad >= 16 and not permiso_padres:
    print('Necesitas el permiso de tus padres para obtener la licencia.')
else:
    print('Eres demasiado joven para conducir.')