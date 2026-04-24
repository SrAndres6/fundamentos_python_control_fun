# =============================================================
# Archivo 20 - Raíz cuadrada por aproximación (Newton-Raphson)
# =============================================================
# Algoritmo iterativo: parte de una estimación inicial y la mejora
# en cada paso hasta que el error sea menor que la precisión deseada.
# Ideal para while porque no sabemos cuántas iteraciones necesitará.

def calcular_raiz_cuadrada(numero, precision=0.0001):
    """
    Calcula la raíz cuadrada usando el método de Newton-Raphson.

    Parámetros:
        numero (float): El número del que se quiere la raíz.
        precision (float): Error máximo aceptable (por defecto 0.0001).

    Retorna:
        float: Aproximación de la raíz cuadrada.
    """
    aproximacion = numero / 2   # Estimación inicial: mitad del número

    # Continúa mientras el error sea mayor que la precisión
    while abs(aproximacion**2 - numero) > precision:
        # Fórmula de Newton para mejorar la aproximación
        aproximacion = (aproximacion + numero / aproximacion) / 2

    return aproximacion


print(f"Raíz cuadrada de 25: {calcular_raiz_cuadrada(25):.6f}")  # 5.000000
print(f"Raíz cuadrada de 7:  {calcular_raiz_cuadrada(7):.6f}")   # 2.645751
