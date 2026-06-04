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

if __name__ == "__main__":
    main()