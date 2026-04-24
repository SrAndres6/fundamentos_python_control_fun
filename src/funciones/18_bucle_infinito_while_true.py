# =============================================================
# Archivo 18 - Bucle infinito controlado con while True
# =============================================================
# 'while True' crea un bucle que nunca termina por sí solo.
# Se controla la salida con 'break' cuando ocurre la condición deseada.
# Es el patrón estándar para menús interactivos.

while True:
    respuesta = input("¿Quieres continuar? (s/n): ").lower()  # .lower() → minúsculas

    if respuesta == "n":
        print("Programa finalizado.")
        break  # Única salida del bucle infinito

    if respuesta == "s":
        print("Continuando...")
    else:
        print("Respuesta no válida. Introduce 's' o 'n'.")
        # Sin break ni continue: el bucle vuelve al inicio automáticamente
