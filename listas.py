from random import randint

#
# Examen de programación basada en Python - 2022
# Nombre: Alex Gheorghe
# Fecha: 2022-12-13
#
# Ejericio 01
#

if __name__ == '__main__':

    # Creamos una lista de 50 números enteros aleatorios
    enteros = []
    for i in range(50):
        enteros.append(randint(1, 100))

    # Mostramos la lista enteros y su número de elementos
    print("Lista enteros:")
    print(enteros)
    print(f"Número de elementos: {len(enteros)}")

    # Creamos otra lista que contenga los elementos de la lista enteros que sean múltiplos de 3 o de 7
    multiplos37 = []
    for i in enteros:
        if i % 3 == 0 or i % 7 == 0:
            multiplos37.append(i)

    # Mostramos la lista multiplos37 y su número de elementos
    print("\nLista multiplos37:")
    print(multiplos37)
    print(f"Número de elementos: {len(multiplos37)}")

    # Creamos una lista que contenga los elementos repetidos de la lista multiplos37
    repe37 = []
    for i in multiplos37:
        if multiplos37.count(i) > 1:
            if i not in repe37:
                repe37.append(i)

    # Mostramos la lista repe37
    print("\nLista repe37:")
    print(repe37)