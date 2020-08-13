# Areas de Figs Geométricas ---------------------------
import os
import math

# Pausa ------------------------------------------------

def pausa():
    print("Presiona <Enter> para continuar")
    input()

# Areas de figuras ------------------------------    
def areaTriangulo(b, h):
# ...

# ....

# Area de un triángulo ------------------------------

def calcularAreaTriangulo():
    os.system("clear")
    print("AREA DE UN TRIANGULO")
    print("====================")
    b = float(input("Base:"))
    h = float(input("Altura:"))

    area = areaTriangulo(b,h)
 
    print(f"Area del Triangulo = {area:5.2f}")
    pausa()

# ...
# Menu principal ----------------------------------------------------------

def menu():
    os.system("clear")
    print("CALCULADORA AREAS")
    print("=================")
    print("1->Area de un triangulo")
    print("2->Area de un cuadrado")
    print("3->Area de un rectangulo")
    print("4->Area de un circulo")
    print("*->Salir")
    opcion = input("Opcion->")

    return opcion

if __name__ == "__main__":

    opcion = "1"
    while opcion != "*":
        opcion = menu()

        if opcion == "1":
            calcularAreaTriangulo()
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
    os.system("clear")
    print("Fin de la calculadora de areas geometricas...")
