# =============================================================
# Archivo 25 - Búsqueda eficiente con break (buscar_elemento)
# =============================================================
# Al encontrar el elemento, retornamos inmediatamente (break implícito).
# Esto evita recorrer el resto de la lista innecesariamente.
# Si el elemento no existe, el bucle termina y retornamos -1.

def buscar_elemento(lista, objetivo):
    """
    Busca un elemento en una lista y retorna su posición.

    Parámetros:
        lista (list): Lista donde se buscará el elemento.
        objetivo: Valor a buscar.

    Retorna:
        int: Índice del elemento si se encuentra, -1 si no existe.
    """
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice   # Encontrado: retornar actúa como break implícito

    return -1   # Solo llega aquí si el bucle terminó sin encontrarlo


numeros = [4, 7, 2, 9, 1, 5]
posicion = buscar_elemento(numeros, 9)
print(f"El elemento se encuentra en la posición: {posicion}")  # 3

posicion = buscar_elemento(numeros, 99)
print(f"El elemento se encuentra en la posición: {posicion}")  # -1
