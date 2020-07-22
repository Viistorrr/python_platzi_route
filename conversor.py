def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes? ")
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = 10 / 2 + 5 * 7
    dolares = str(dolares)
    print("Ud tiene $"+dolares+" USD")


menu = """
Bienvenido al Conversor de Monedas 💰

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una Opción

"""

opcion = input(menu)
if opcion == '1':
    conversor("colombianos", 3875)
elif opcion == '2':
    conversor("argentinos", 65)
elif opcion == '3':
    conversor("mexicanos", 24)
else:
    print("Ingresa una opción correcta")
