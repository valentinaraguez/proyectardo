import random

def verificar_intento(palabra_secreta, intento):
    resultado = []
    for i in range(len(intento)):
        if intento[i] == palabra_secreta[i]:
            resultado.append("🟩")
        elif intento[i] in palabra_secreta:
            resultado.append("🟨")
        else:
            resultado.append("⬛")
    return resultado

def jugar():
    palabras = [
        "sol", "mar", "pan", "luz", "ave", 
        "rio", "sal", "pie", "mes", "dia",
        "gol", "bar", "voz", "ley", "tos",
        "uno", "sur", "fin", "mal", "dos"
    ]
    palabra_secreta = random.choice(palabras).upper()
    intentos_maximos = 4
    intentos = 0

    print("\n" + "=" * 30)
    print("wordle base".center(30))
    print("=" * 30)

    while intentos < intentos_maximos:
        intento = input("\ningresa una palabra (3 letras): ").upper().strip()

        if len(intento) != 3 or not intento.isalpha():
            print("x error: deben ser 3 letras")
            continue

        resultado = verificar_intento(palabra_secreta, intento)

        print()
        print(" ".join(intento))
        print(" ".join(resultado))

        if intento == palabra_secreta:
            print("\nganaste")
            return

        intentos += 1
        print(f"intentos restantes: {intentos_maximos - intentos}")

    print(f"\ngame over. la palabra era: {palabra_secreta}")

def main():
    while True:
        jugar()
        continuar = input("\njugar de nuevo? (s/n): ").lower().strip()
        if continuar not in ["s", "si", "sí"]:
            print("\nnos vemos")
            break

def mostrar_menu():
    
    print("\n" + "=" * 50)
    print("bienvenido a wordle".center(50))
    print("=" * 50)

    print("\n" + "=" * 50)
    print("\n 1- Facil (3 letras)")
    print("\n 2- Normal (4 letras)")
    print("\n 3- Medio (5 letras)")
    print("\n 4- Dificil (6 letras)")
    print("\n 5- Experto (7 letras)")
    print("\n 6- Aleatorio")
    print("\n 0- Salir")

    while True:
        opcion = input("\nSelecciona una opción: ").strip()
        if opcion == "1":
            print("\nModo Facil seleccionado.")
            return 3
        elif opcion == "2":
            print("\nModo Normal seleccionado.")
            return 4
        elif opcion == "3":
            print("\nModo Medio seleccionado.")
            return 5
        elif opcion == "4":
            print("\nModo Dificil seleccionado.")
            return 6
        elif opcion == "5":
            print("\nModo Experto seleccionado.")
            return 7
        elif opcion == "6":
            print("\nModo Aleatorio seleccionado.")
            return random.randint(3, 7)
        elif opcion == "0":
            print("\nGracias por jugar. ¡Hasta luego!")
            exit()
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")



if __name__ == "__main__":
    main()