# =============================================================
# Archivo 16 - Juego de adivinanza con while
# =============================================================
# El bucle continúa mientras NO se haya adivinado Y queden intentos.
# La condición tiene dos partes con 'and': ambas deben ser True
# para que el bucle continúe ejecutándose.

import random  # Para generar el número secreto aleatorio

objetivo = random.randint(1, 10)  # Número secreto entre 1 y 10
intentos = 0
adivinado = False

while not adivinado and intentos < 3:  # Máximo 3 intentos
    intentos += 1
    numero = int(input(f"Intento {intentos}/3: Adivina un número del 1 al 10: "))

    if numero == objetivo:
        print(f"¡Correcto! Has adivinado en {intentos} intentos.")
        adivinado = True
    else:
        # Operador ternario: elige "mayor" o "menor" según el caso
        pista = "mayor" if numero < objetivo else "menor"
        print(f"Incorrecto. El número es {pista} que {numero}.")

# Si salió del while sin adivinar, muestra el número correcto
if not adivinado:
    print(f"Se acabaron los intentos. El número era {objetivo}.")
