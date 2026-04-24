# Se utiliza la condición ternaria para verificar si la edad es mayor o igual a 18.
edad = 20
categoria = "Menor" if edad < 18 else ("Joven Adulto" if edad < 30 else "Adulto")
print(categoria)