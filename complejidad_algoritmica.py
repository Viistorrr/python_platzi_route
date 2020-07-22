import time


def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta


def factorial_r(n):  # factorial recursivo
    if n == 1:
        return

    return n * factorial(n-1)


if __name__ == '__main__':
    n = 50000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final-comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final-comienzo)
