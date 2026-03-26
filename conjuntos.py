from lista_ligada import ListaLigada

class Conjunto:
    def __init__(self):
        self.lista = ListaLigada()

    def agregar(self, dato):
        if not self.lista.contiene(dato):
            self.lista.insertar(dato)

    def contiene(self, dato):
        return self.lista.contiene(dato)

    def mostrar(self):
        self.lista.mostrar()

    def get_cabeza(self):
        return self.lista.cabeza
