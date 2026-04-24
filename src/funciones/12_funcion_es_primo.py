# =============================================================
# Archivo 12 - Números primos con función es_primo()
# =============================================================
# Un número primo solo es divisible por 1 y por sí mismo.
# Optimización: solo verificamos divisores hasta la raíz cuadrada.
# Si encontramos un divisor, retornamos False inmediatamente.

def es_primo(num):
    """
    Verifica si un número es primo.

    Parámetros:
        num (int): El número a evaluar.

    Retorna:
        bool: True si es primo, False si no lo es.
    """
    if num < 2:
        return False  # Números menores a 2 no son primos

    # Solo verificamos hasta la raíz cuadrada (optimización)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Encontramos un divisor: no es primo
    return True  # Sin divisores: es primo


# Recopilar todos los primos entre 2 y 19
primos = []
for num in range(2, 20):
    if es_primo(num):
        primos.append(num)

print(f"Números primos entre 2 y 19: {primos}")
# Resultado: [2, 3, 5, 7, 11, 13, 17, 19]
