# Función que verifica si un número es par
def es_par(numero):
    return numero % 2 == 0

# Función que convierte temperatura de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Asignar una función a una variable
convertir = celsius_a_fahrenheit
temperatura_f = convertir(25)  # Equivalente a celsius_a_fahrenheit(25)
print(f"25°C equivalen a {temperatura_f}°F")  # Imprime: 25°C equivalen a 77.0°F