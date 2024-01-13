import random

def obtener_palabra_aleatoria():
    palabras = ["leon", "zebra", "camello", "perro", "gato", "aguila", "camaleon"]
    return list(random.choice(palabras))

def jugar_ahorcado():
    palabra_secreta = obtener_palabra_aleatoria()
    letras_adivinadas = set()
    intentos_maximos = 6
    intentos_realizados = 0

    print("¡Bienvenido al juego del Ahorcado de animales!")
    print("_ " * len(palabra_secreta))

    while True:
        letra = input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta con otra.")
            continue

        letras_adivinadas.add(letra)

        if letra not in palabra_secreta: 
            intentos_realizados += 1
            print(f"Incorrecto. Intentos restantes: {intentos_maximos - intentos_realizados}")
        else:
            print("Correcto. ¡Adivinaste una letra!")

        palabra_oculta = "".join([letra if letra in letras_adivinadas else "_ " for letra in palabra_secreta])
        print(palabra_oculta)

        if palabra_oculta.replace(" ", "") == "".join(palabra_secreta):
            print("¡Felicidades! ¡Adivinaste la palabra!")
            break

        if intentos_realizados == intentos_maximos:
            print(f"Agotaste tus intentos. La palabra era '{''.join(palabra_secreta)}'. ¡Perdiste!")
            break

if __name__ == "__main__":
    jugar_ahorcado()
