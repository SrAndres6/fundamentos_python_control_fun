# =============================================================
# Archivo 30 - Evitar división por cero con continue
# =============================================================
# Si intentamos dividir por 0 Python lanza ZeroDivisionError.
# Usamos continue para detectar el 0 antes y saltar esa iteración,
# evitando el error sin necesidad de un bloque try/except.

numeros = [1, 2, 0, 4, 0, 6, 7]

for num in numeros:
    if num == 0:
        print("Omitiendo división por cero")
        continue            # Saltamos la división cuando num es 0

    resultado = 10 / num    # Solo se ejecuta si num != 0
    print(f"10 / {num} = {resultado}")

# Resultado:
# 10 / 1 = 10.0
# 10 / 2 = 5.0
# Omitiendo división por cero
# 10 / 4 = 2.5
# Omitiendo división por cero
# 10 / 6 = 1.666...
# 10 / 7 = 1.428...
