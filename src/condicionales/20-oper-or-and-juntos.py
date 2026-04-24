# Se utiliza los operadores or y and juntos para verificar si la edad y los ingresos son mayores o iguales a 18 y 20000 respectivamente.
edad = 17
permiso_parental = True

if (edad >= 18) or (edad >= 16 and permiso_parental):
    print("Puedes obtener la licencia de conducir.")
else:
    print("No cumples los requisitos para la licencia.")