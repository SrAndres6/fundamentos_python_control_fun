# =============================================================
# Archivo 33 - continue en bucles anidados
# =============================================================
# IMPORTANTE: continue solo afecta al bucle más INTERNO donde está.
# El bucle externo continúa ejecutándose normalmente.
# Cada grupo completa sus elementos saltando el 3.

for i in range(1, 4):               # Bucle externo: grupos 1, 2, 3
    print(f"Grupo {i}:")

    for j in range(1, 6):           # Bucle interno: elementos 1 al 5
        if j == 3:
            print("  Saltando el elemento 3")
            continue                # Solo salta en el bucle interno (j)
        print(f"  Elemento {j}")

    print("Fin del grupo\n")        # Esto sí se ejecuta para cada grupo
