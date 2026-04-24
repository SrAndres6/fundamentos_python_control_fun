# =============================================================
# Archivo 21 - Validación robusta de entrada con rango
# =============================================================
# Combina while True con try/except para manejar dos tipos de error:
#   1. El usuario escribe letras en vez de números (ValueError)
#   2. El número está fuera del rango permitido
# El bucle solo termina cuando la entrada es completamente válida.

def obtener_numero_en_rango(mensaje, minimo, maximo):
    """
    Solicita un número entero dentro de un rango específico.
    Repite la solicitud hasta recibir un valor válido.

    Parámetros:
        mensaje (str): Texto mostrado al usuario al pedir el dato.
        minimo (int): Valor mínimo aceptable (inclusive).
        maximo (int): Valor máximo aceptable (inclusive).

    Retorna:
        int: El número válido ingresado por el usuario.
    """
    while True:
        try:
            valor = int(input(mensaje))       # Lanza ValueError si no es número
            if minimo <= valor <= maximo:
                return valor                  # Válido: salimos del bucle
            print(f"Error: El número debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Error: Debes introducir un número entero.")
        # Si hubo error, el bucle continúa y vuelve a pedir el dato


edad = obtener_numero_en_rango("Introduce tu edad (0-120): ", 0, 120)
print(f"Edad registrada: {edad} años")
