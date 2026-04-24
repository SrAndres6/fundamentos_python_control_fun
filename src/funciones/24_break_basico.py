# =============================================================
# Archivo 24 - Sentencia break básica
# =============================================================
# 'break' termina el bucle COMPLETAMENTE de forma inmediata.
# El código que sigue después del bucle continúa ejecutándose.
# Solo afecta al bucle más interno donde se encuentra.

for numero in range(1, 11):
    if numero == 5:
        print("¡Encontrado el 5! Saliendo del bucle...")
        break               # Termina el bucle: no procesa 6, 7, 8, 9, 10
    print(f"Número actual: {numero}")

print("Bucle terminado")  # Esto sí se ejecuta después del break

# Resultado:
# Número actual: 1
# Número actual: 2
# Número actual: 3
# Número actual: 4
# ¡Encontrado el 5! Saliendo del bucle...
# Bucle terminado
