# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('¡Estoy aprendiendo a usar funciones!')

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

# opcion = int(input('Elige una opción (1,2,3): '))
# if opcion == 1:
#     print('Hola')
#     print('Como estás')
#     print('Elegiste la opción 1')
#     print('Adios')


def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes? : ")
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = str(round(dolares,2))
    print(" Tienes $"+ dolares + " dólares")

menu = """
Bienvenido al conversor de moneda 🤗

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción:
"""

opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos",3750)
elif opcion == 2:    
    conversor("Argentinos",65)
elif opcion == 3:    
    conversor("Mexicanos",24)
else: 
    print("Ingresa una opción correcta" )
    