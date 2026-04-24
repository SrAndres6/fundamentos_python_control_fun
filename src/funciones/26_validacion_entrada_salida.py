# =============================================================
# Archivo 26 - Validación de entrada con salida por comando
# =============================================================
# Bucle infinito que captura texto del usuario repetidamente.
# El usuario puede escribir 'salir' en cualquier momento para terminar.
# .lower() convierte la entrada a minúsculas para comparar sin importar mayúsculas.

while True:
    entrada = input("Escribe algo (o 'salir' para terminar): ")

    if entrada.lower() == 'salir':
        print("Programa terminado.")
        break           # Salimos del while True

    print(f"Has escrito: {entrada}")
    # El bucle continúa hasta que el usuario escriba 'salir'
