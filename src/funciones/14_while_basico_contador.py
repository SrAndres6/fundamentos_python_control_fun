# =============================================================
# Archivo 14 - Bucle while básico (contador)
# =============================================================
# El bucle 'while' repite el bloque MIENTRAS la condición sea True.
# IMPORTANTE: la variable de control (contador) debe actualizarse
# dentro del bucle para evitar un bucle infinito.

contador = 1  # Variable de control: comienza en 1

while contador <= 5:      # Condición: continúa mientras sea <= 5
    print(contador)
    contador += 1         # Actualización obligatoria: suma 1 cada vez

# Resultado:
# 1
# 2
# 3
# 4
# 5
