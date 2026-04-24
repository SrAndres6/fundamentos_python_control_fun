# =============================================================
# Archivo 15 - Validar entrada del usuario con while
# =============================================================
# Usamos while para seguir pidiendo datos hasta que el usuario
# ingrese algo válido. .isdigit() verifica que la cadena
# sea un número entero positivo.

entrada = ""  # Iniciamos vacío para que el while arranque

while not entrada.isdigit():  # Repite mientras NO sea un número
    entrada = input("Introduce un número: ")

print(f"Has introducido el número: {entrada}")
# El bucle termina solo cuando el usuario escribe un número válido
