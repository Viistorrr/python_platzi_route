objetivo = int(input("Escoge un numero: "))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto+bajo)/2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f"BAJO={bajo} ALTO={alto} RESPUESTA={respuesta}")
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (alto+bajo)/2

print(f"La raiz cuadrada del objetivo es {respuesta}")
