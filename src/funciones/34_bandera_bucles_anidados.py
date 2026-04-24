# =============================================================
# Archivo 34 - Bandera para salir de múltiples bucles anidados
# =============================================================
# break solo sale del bucle más interno. Para salir del externo
# usamos una variable booleana (bandera) que se verifica en ambos bucles.
# Cuando la bandera es True, ambos bucles ejecutan su break.

encontrado = False  # Bandera: False = no encontrado aún

for i in range(5):
    for j in range(5):
        if i * j > 10:
            print(f"Valor encontrado: {i} * {j} = {i*j}")
            encontrado = True
            break           # Sale del bucle interno (j)

    if encontrado:
        break               # Sale del bucle externo (i) gracias a la bandera

print(f"Búsqueda terminada. Encontrado: {encontrado}")
