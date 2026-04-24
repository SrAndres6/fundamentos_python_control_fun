# Se utiliza la condición if-elif-else para determinar si una persona es menor de edad, adulto o mayor de 65 años.
edad = 45

if edad < 18:
    print("Eres menor de edad.")
elif 18 <= edad < 65:
    print("Eres adulto.")
else:
    print("Eres mayor de 65 años.")