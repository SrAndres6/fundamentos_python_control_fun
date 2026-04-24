# =============================================================
# Archivo 22 - Triángulo de asteriscos con while
# =============================================================
# En cada iteración imprimimos una fila con tantos '*' como indica 'fila'.
# El operador * con strings repite el carácter N veces.
# 'fila' funciona como variable de control del bucle.

def imprimir_triangulo(altura):
    """
    Imprime un triángulo rectángulo de asteriscos.

    Parámetros:
        altura (int): Número de filas del triángulo.

    Ejemplo para altura=5:
        *
        **
        ***
        ****
        *****
    """
    fila = 1                    # Empezamos con 1 asterisco

    while fila <= altura:
        print("*" * fila)       # Repite '*' tantas veces como indica 'fila'
        fila += 1               # Aumentamos para la siguiente fila


imprimir_triangulo(5)
