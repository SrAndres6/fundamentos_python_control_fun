# Se utiliza la función any() para verificar si al menos un elemento del iterable
# es True o tiene un valor considerado "truthy" (por ejemplo, un número distinto de cero,
# una cadena no vacía, etc.).
numeros = [0, 0, 1, 0]

if any(numeros):
    print("Al menos un número es no cero.")