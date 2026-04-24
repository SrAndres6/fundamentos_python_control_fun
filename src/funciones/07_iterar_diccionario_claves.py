# =============================================================
# Archivo 07 - Iterando sobre diccionarios (claves)
# =============================================================
# Al iterar un diccionario con for, por defecto se recorren
# solo las CLAVES. Para obtener el valor usamos dict[clave].

usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}

# Iterando solo las claves (comportamiento por defecto)
for clave in usuario:
    print(f"Clave: {clave}, Valor: {usuario[clave]}")

# Resultado:
# Clave: nombre, Valor: Laura
# Clave: edad, Valor: 28
# Clave: ciudad, Valor: Madrid
