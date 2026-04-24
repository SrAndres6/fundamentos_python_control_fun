# =============================================================
# Archivo 09 - Comprensiones de listas
# =============================================================
# Las comprensiones de listas permiten crear listas en una sola línea
# usando la sintaxis del bucle for. Son más compactas y pythónicas.
# Sintaxis: [expresion for variable in iterable if condicion]

# Crear lista con los cuadrados de los números del 1 al 5
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]

# Filtrar elementos: solo números pares del 0 al 9
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
