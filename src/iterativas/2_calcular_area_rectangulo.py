def calcular_area_rectangulo(base, altura):
    """
    Función que calcula el área de un rectángulo. 
    Recibe la base y la altura como parámetros y devuelve el área.
    """
    area = base * altura
    return area

# Uso de la función
resultado = calcular_area_rectangulo(5, 3)
print(f"El área del rectángulo es: {resultado}")  # Imprime: El área del rectángulo es: 15