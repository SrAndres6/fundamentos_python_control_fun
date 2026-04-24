# =============================================================
# Archivo 05 - Función enumerate()
# =============================================================
# enumerate() es la forma más elegante de obtener índice y valor
# al mismo tiempo. Evita tener que usar range(len(...)).
# Devuelve pares (índice, valor) en cada iteración.

nombres = ["Ana", "Carlos", "Elena"]

for indice, nombre in enumerate(nombres):
    print(f"Posición {indice}: {nombre}")

# Resultado:
# Posición 0: Ana
# Posición 1: Carlos
# Posición 2: Elena
