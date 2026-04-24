# =============================================================
# Archivo 04 - Iterando sobre índices con range() y len()
# =============================================================
# Cuando necesitamos el índice (posición) y el valor al mismo tiempo,
# combinamos range() con len() para acceder a cada elemento por posición.

nombres = ["Ana", "Carlos", "Elena"]

for i in range(len(nombres)):       # range(3) → 0, 1, 2
    print(f"Posición {i}: {nombres[i]}")  # Accedemos al elemento por índice

# Resultado:
# Posición 0: Ana
# Posición 1: Carlos
# Posición 2: Elena
