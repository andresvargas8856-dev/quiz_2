class Conjunto:
    def __init__(self):
        self.cabeza = None  # inicio de la lista ligada

    # =========================
    # AGREGAR ELEMENTO (sin duplicados)
    # =========================
    def agregar(self, dato):
        if not self.contiene(dato):  # evitamos repetidos
            nuevo = Nodo(dato)

            if self.cabeza is None:
                self.cabeza = nuevo
            else:
                actual = self.cabeza
                while actual.siguiente:
                    actual = actual.siguiente
                actual.siguiente = nuevo

    # =========================
    # BUSCAR ELEMENTO
    # =========================
    def contiene(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    # =========================
    # ELIMINAR ELEMENTO (IMPORTANTE)
    # =========================
    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None  # sirve para reconectar la lista

        while actual:
            if actual.dato == dato:
                # CASO 1: eliminar el primer nodo
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    # CASO 2: eliminar nodo intermedio o final
                    anterior.siguiente = actual.siguiente
                return True  # eliminado correctamente

            anterior = actual
            actual = actual.siguiente

        return False  # no se encontró el dato
