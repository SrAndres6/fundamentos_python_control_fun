# =============================================================
# Archivo 03 - range() con start, stop y step
# =============================================================
# range() acepta hasta 3 parámetros:
#   range(stop)             → desde 0 hasta stop-1
#   range(start, stop)      → desde start hasta stop-1
#   range(start, stop, step)→ desde start hasta stop-1, saltando de step en step

# Números del 3 al 7
for i in range(3, 8):
    print(i, end=" ")  # end=" " imprime en la misma línea
print()  # Salto de línea al final
# Resultado: 3 4 5 6 7

# Números pares del 2 al 10 (step=2)
for i in range(2, 11, 2):
    print(i, end=" ")
print()
# Resultado: 2 4 6 8 10

# Cuenta regresiva del 10 al 1 (step=-1)
for i in range(10, 0, -1):
    print(i, end=" ")
print()
# Resultado: 10 9 8 7 6 5 4 3 2 1
