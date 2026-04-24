# =============================================================
# Archivo 19 - Calcular factorial con while
# =============================================================
# El factorial de n (n!) = n × (n-1) × (n-2) × ... × 1
# Usamos while porque n cambia en cada iteración hasta llegar a 0.
# 'resultado' es la variable acumuladora del producto.

def calcular_factorial(n):
    """
    Calcula el factorial de un número entero positivo.

    Parámetros:
        n (int): El número del que se calcula el factorial.

    Retorna:
        int: El resultado de n!

    Ejemplo: factorial(5) = 5 × 4 × 3 × 2 × 1 = 120
    """
    resultado = 1       # Iniciamos en 1 (elemento neutro de la multiplicación)

    while n > 0:
        resultado *= n  # Multiplicación acumulativa: resultado = resultado * n
        n -= 1          # Decrementamos n para avanzar hacia la condición de salida

    return resultado


numero = 5
print(f"El factorial de {numero} es {calcular_factorial(numero)}")
# Resultado: El factorial de 5 es 120
