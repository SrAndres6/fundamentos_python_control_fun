# =============================================================
# Archivo 27 - Verificación de primo optimizada con break
# =============================================================
# En cuanto encontramos UN divisor, ya sabemos que no es primo.
# Salimos inmediatamente con return False (break implícito).
# Verificar solo hasta la raíz cuadrada reduce el número de operaciones.

def es_primo(n):
    """
    Verifica si un número es primo de forma eficiente.

    Parámetros:
        n (int): Número a evaluar.

    Retorna:
        bool: True si es primo, False si no.

    Optimización: solo verifica divisores hasta sqrt(n).
    """
    if n < 2:
        return False    # Menores de 2 no son primos por definición

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Divisor encontrado: salimos inmediatamente

    return True           # Sin divisores: confirmado primo


# Probamos varios números
for num in [2, 7, 10, 13, 25]:
    resultado = "primo" if es_primo(num) else "no primo"
    print(f"{num} es {resultado}")
