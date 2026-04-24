# =============================================================
# Archivo 10 - Bucles for anidados (tabla de multiplicar)
# =============================================================
# Los bucles anidados tienen un bucle dentro de otro.
# El bucle interno se ejecuta completo por cada iteración del externo.
# Son útiles para trabajar con estructuras de datos bidimensionales.

# Tabla de multiplicación 3x3
for i in range(1, 4):           # Bucle externo: filas (1, 2, 3)
    for j in range(1, 4):       # Bucle interno: columnas (1, 2, 3)
        print(f"{i} × {j} = {i*j}", end="\t")  # \t = tabulación
    print()  # Salto de línea al terminar cada fila

# Resultado:
# 1 × 1 = 1    1 × 2 = 2    1 × 3 = 3
# 2 × 1 = 2    2 × 2 = 4    2 × 3 = 6
# 3 × 1 = 3    3 × 2 = 6    3 × 3 = 9
