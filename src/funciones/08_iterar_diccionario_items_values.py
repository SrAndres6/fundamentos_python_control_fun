# =============================================================
# Archivo 08 - Iterando diccionarios con .items() y .values()
# =============================================================
# Python ofrece métodos para iterar diccionarios de distintas formas:
#   .items()  → pares (clave, valor)
#   .keys()   → solo claves
#   .values() → solo valores

usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}

# Iterando pares clave-valor con .items()
print("--- items() ---")
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# Iterando solo valores con .values()
print("--- values() ---")
for valor in usuario.values():
    print(valor)

# Resultado:
# --- items() ---
# nombre: Laura
# edad: 28
# ciudad: Madrid
# --- values() ---
# Laura
# 28
# Madrid
