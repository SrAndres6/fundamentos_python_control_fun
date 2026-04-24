# =============================================================
# Archivo 31 - Validar datos numéricos con continue
# =============================================================
# Procesamos una lista mixta de strings.
# .isdigit() retorna True solo si todos los caracteres son dígitos.
# Con continue saltamos los valores no numéricos y sumamos los válidos.

datos = ["25", "error", "42", "texto", "17"]

suma = 0
for valor in datos:
    if not valor.isdigit():             # Si NO es un número...
        print(f"Valor no numérico ignorado: '{valor}'")
        continue                        # ...lo saltamos

    suma += int(valor)                  # Solo suma si es numérico válido

print(f"La suma de los valores válidos es: {suma}")
# Resultado:
# Valor no numérico ignorado: 'error'
# Valor no numérico ignorado: 'texto'
# La suma de los valores válidos es: 84
