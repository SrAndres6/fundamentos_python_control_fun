# =============================================================
# Archivo 23 - Comparación: while vs for para la misma tarea
# =============================================================
# Muchos bucles pueden escribirse con while o con for.
# Regla general:
#   - Usa FOR cuando conoces el número exacto de iteraciones.
#   - Usa WHILE cuando la condición depende de eventos o cálculos.

# Versión con WHILE: requiere variable de control manual
suma = 0
i = 1
while i <= 10:
    suma += i
    i += 1          # Hay que acordarse de incrementar manualmente
print(f"Suma (while): {suma}")  # 55

# Versión equivalente con FOR: más concisa y menos propensa a errores
suma = 0
for i in range(1, 11):
    suma += i       # range() maneja automáticamente el incremento
print(f"Suma (for):   {suma}")  # 55

# Ambas producen el mismo resultado: 55
