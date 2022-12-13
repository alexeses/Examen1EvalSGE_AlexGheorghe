
if __name__ == '__main__':
  # Creamos un diccionario que asocie cada palabra en español con su traducción en inglés
  diccionario = {"hola": "hello", "adiós": "bye", "amor": "love", "cielo": "sky", "mar": "sea", "día": "day",
                 "noche": "night", "año": "year"}

  # Mostramos el diccionario completo
  print("Diccionario completo:")
  print(diccionario)

  # Mostramos por separado todas las claves y todos los valores del diccionario
  print("\nClaves del diccionario:")
  print(diccionario.keys())

  print("\nValores del diccionario:")
  print(diccionario.values())

  # Pedimos al usuario que ingrese una palabra en español
  palabra_espanol = input("\nIngrese una palabra en español: ")

  # Mostramos la traducción de la palabra en inglés, si existe
  if palabra_espanol in diccionario:
      print(f"La palabra {palabra_espanol} es {diccionario[palabra_espanol]} en inglés")
  else:
      print(f"La palabra {palabra_espanol} no se encuentra en el diccionario")
