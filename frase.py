
if __name__ == '__main__':
    # Pedimos al usuario que ingrese una frase y una letra
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra: ")

    # Contamos la cantidad de veces que aparece la letra en la frase
    veces = frase.count(letra)

    # Mostramos el resultado
    print(f"Frase: {frase}  Letra: {letra}")
    print(f"La letra {letra} aparece {veces} veces en la frase {frase}")

    # Mostramos la frase completa sin dicha letra
    frase_sin_letra = frase.replace(letra, "")
    print(f"La frase anterior sin dicha letra es: {frase_sin_letra}")