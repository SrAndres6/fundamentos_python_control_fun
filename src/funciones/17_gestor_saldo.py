# =============================================================
# Archivo 17 - Gestor de saldo con while, break y continue
# =============================================================
# La condición (saldo > 0) cambia dinámicamente dentro del bucle.
# Usamos break para salir si el usuario ingresa 0,
# y continue para volver al inicio si el gasto supera el saldo.

saldo = 1000  # Saldo inicial

while saldo > 0:  # Continúa mientras haya saldo
    print(f"Saldo actual: {saldo}€")
    gasto = float(input("Introduce la cantidad a gastar (0 para salir): "))

    if gasto == 0:
        break  # El usuario quiere salir: terminamos el bucle

    if gasto > saldo:
        print("No tienes suficiente saldo.")
        continue  # Volvemos al inicio sin descontar nada

    saldo -= gasto  # Descontamos el gasto del saldo

print(f"Saldo final: {saldo}€")
