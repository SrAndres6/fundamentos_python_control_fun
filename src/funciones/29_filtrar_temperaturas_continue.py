# =============================================================
# Archivo 29 - Filtrar temperaturas negativas con continue
# =============================================================
# Usamos continue para saltar los valores que no nos interesan
# y procesar solo los que cumplen la condición (temp > 0).
# Es más limpio que anidar el código dentro de un if.

temperaturas = [22, -5, 28, 31, -15, 19, 26, -8]

print("Temperaturas positivas:")
for temp in temperaturas:
    if temp <= 0:
        continue        # Saltamos temperaturas negativas o cero
    print(f"{temp}°C")  # Solo se imprime si pasó el filtro

# Resultado:
# Temperaturas positivas:
# 22°C
# 28°C
# 31°C
# 19°C
# 26°C
