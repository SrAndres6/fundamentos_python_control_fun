# =============================================================
# Archivo 11 - Suma de los primeros n números
# =============================================================
# Usamos una variable acumuladora 'suma' que empieza en 0.
# En cada iteración le sumamos el número actual del rango.
# range(1, n+1) genera del 1 al n inclusive.

n = 10
suma = 0  # Variable acumuladora inicializada en 0

for i in range(1, n + 1):  # Del 1 al 10 inclusive
    suma += i              # suma = suma + i

print(f"La suma de los primeros {n} números es: {suma}")
# Resultado: La suma de los primeros 10 números es: 55
