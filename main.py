from conjunto import Conjunto
from operaciones_conjunto import OperacionesConjunto

def main():
    A = Conjunto()
    B = Conjunto()

    A.agregar(1)
    A.agregar(2)
    A.agregar(3)

    B.agregar(3)
    B.agregar(4)
    B.agregar(5)

    print("Conjunto A:")
    A.mostrar()

    print("Conjunto B:")
    B.mostrar()

    union = OperacionesConjunto.union(A, B)
    print("Union:")
    union.mostrar()

    inter = OperacionesConjunto.interseccion(A, B)
    print("Interseccion:")
    inter.mostrar()

    dif = OperacionesConjunto.diferencia(A, B)
    print("Diferencia A - B:")
    dif.mostrar()

if __name__ == "__main__":
    main()
