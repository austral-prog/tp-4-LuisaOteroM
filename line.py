import math
def line():
    a = float(imput("Ingrese el coeficiente A: "))
    b = float(imput("Ingrese el coeficiente B: "))
    c = float(imput("Ingrese el coeficiente X1: "))
    d = float(imput("Ingrese el coeficiente X2: "))

    print(f"El coeficiente A de su ecuacion de la recta es: {a}")
    print(f"El coeficiente B de su ecuacion de la recta es: {b}")
    print(f"El coeficiente X1 de su ecuacion de la recta es: {x1}")
    print(f"El coeficiente X2 de su ecuacion de la recta es: {x2}")
    print()

    Y1 = A*X1 + B
    Y2 = A*X2 + B

    print("Para la siguiente ecuación:")
    print()
    print(f"\tY={A}X + {B}\n")

    print("Dados los siguientes puntos:")
    print(f"\tP1={x1}, {x2}")
    print(f"\tP1={y1}, {y2}")

    P1 = (X1, Y2)
    P1 = (X2, Y2)

    distancia = math.distancia(P1, P2)
    print(f"La distancia entre ellos es {distancia}")
