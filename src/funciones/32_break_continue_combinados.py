# =============================================================
# Archivo 32 - break y continue combinados en el mismo bucle
# =============================================================
# continue: omite múltiplos de 3 y pasa al siguiente número.
# break: detiene todo el proceso si la suma supera el límite.
# Ambos pueden coexistir en el mismo bucle con lógicas distintas.

numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
limite = 50
suma = 0

for num in numeros:
    if num % 3 == 0:                        # Si es múltiplo de 3...
        print(f"Omitiendo {num} (múltiplo de 3)")
        continue                            # ...lo ignoramos y seguimos

    suma += num                             # Sumamos si pasó el filtro
    print(f"Añadiendo {num}: suma = {suma}")

    if suma > limite:                       # Si superamos el límite...
        print(f"Límite de {limite} superado")
        break                               # ...detenemos todo el bucle
