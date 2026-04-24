# =============================================================
# Archivo 28 - Sentencia continue básica (imprimir impares)
# =============================================================
# 'continue' NO termina el bucle, solo salta la iteración ACTUAL
# y pasa directamente a la siguiente.
# Los números pares se saltan; los impares se imprimen.

for numero in range(1, 11):
    if numero % 2 == 0:     # Si el número es par...
        continue            # ...saltamos esta iteración (no se imprime)
    print(f"Número impar: {numero}")

# Resultado:
# Número impar: 1
# Número impar: 3
# Número impar: 5
# Número impar: 7
# Número impar: 9
