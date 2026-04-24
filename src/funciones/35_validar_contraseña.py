# =============================================================
# Archivo 35 - Validación de contraseñas con break y continue
# =============================================================
# Recorre cada carácter de la contraseña verificando requisitos.
# continue salta al siguiente carácter en cuanto confirma un requisito,
# evitando verificaciones redundantes en el mismo carácter.

def validar_contraseña(contraseña):
    """
    Verifica si una contraseña cumple los requisitos mínimos de seguridad:
    - Al menos 8 caracteres
    - Al menos una letra mayúscula
    - Al menos una letra minúscula
    - Al menos un número

    Parámetros:
        contraseña (str): La contraseña a validar.

    Retorna:
        bool: True si cumple todos los requisitos, False si no.
    """
    if len(contraseña) < 8:
        return False        # Muy corta: no necesitamos revisar más

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
            continue        # Requisito verificado: pasamos al siguiente carácter

        if caracter.islower():
            tiene_minuscula = True
            continue

        if caracter.isdigit():
            tiene_numero = True

    return tiene_mayuscula and tiene_minuscula and tiene_numero


# Probamos varias contraseñas
contraseñas = ["abc123", "Password", "Password1", "pass123", "PASS123"]
for pwd in contraseñas:
    estado = "válida ✓" if validar_contraseña(pwd) else "NO válida ✗"
    print(f"'{pwd}': {estado}")
