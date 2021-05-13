#
menu = """
Bienvenido al conversor de moneda 🤗

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción:
"""

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuántos pesos colombianos tienes? : ")
    pesos = float(pesos)
    valor_dolar = 3757
    dolares = pesos/valor_dolar
    dolares = str(round(dolares, 2))
    print(" Tienes $" + dolares + " dólares")
if opcion == 2:
    pesos = input("¿Cuántos pesos argentinos tienes? : ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos/valor_dolar
    dolares = str(round(dolares, 2))
    print(" Tienes $" + dolares + " dólares")
if opcion == 3:
    pesos = input("¿Cuántos pesos mexicanos tienes? : ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos/valor_dolar
    dolares = str(round(dolares, 2))
    print(" Tienes $" + dolares + " dólares")
else:
    pass
