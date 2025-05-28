def leap_year():
    year = int(imput("Ingrese un año:"))
    if year % 400 == 0:
        print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")
