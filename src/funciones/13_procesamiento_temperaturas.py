# =============================================================
# Archivo 13 - Procesamiento de datos de temperatura
# =============================================================
# Ejemplo práctico que combina: max(), index(), sum(), len()
# y un bucle for para analizar datos de temperatura semanales.

temperaturas = [22, 19, 24, 25, 21, 23, 20]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Encontrar el día más caluroso
max_temp = max(temperaturas)                  # Temperatura máxima
indice_max = temperaturas.index(max_temp)     # Posición del máximo
print(f"El día más caluroso fue {dias[indice_max]} con {max_temp}°C")

# Calcular temperatura promedio
promedio = sum(temperaturas) / len(temperaturas)
print(f"Temperatura promedio: {promedio:.1f}°C")  # :.1f = 1 decimal

# Mostrar días con temperatura por encima del promedio
for i in range(len(dias)):
    if temperaturas[i] > promedio:
        print(f"{dias[i]}: {temperaturas[i]}°C (por encima del promedio)")
