# Contador = 0
# print('2 elevador a ' + str(Contador) + ' es igual a ' + str((2**Contador)))

def run():
    LIMITE = 1000000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('2 elevador a ' + str(contador) + ' es igual a ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador



if __name__ == '__main__':
    run() 