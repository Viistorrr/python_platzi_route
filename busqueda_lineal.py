import random


def busqueda_lineal(lista, objetivo):
    match = False
    for elemento in lista:
        if elemento == objetivo:
            match = True
            break  # no cambia la complejidad algoritmica. Siempre se debe pensar en el peor caso

    return match


if __name__ == '__main__':
    tamano_de_lista = int(input("De que tamano sera la lista? "))
    objetivo = int(input("Que numero quieres encontrar?"))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(
        f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')
