class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print("Ando caminando")


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)  # se hace referencia a la Persona, que es la clase

        def avanza(self):  # debe tener los mismos parametros de la clase padre
            print("Me estoy moviendo en bicicleta")


def main():
    persona = Persona('Victor')
    persona.avanza()

    ciclista = Ciclista('Daniela')
    ciclista.avanza()


if __name__ == '__main__':
    main()
