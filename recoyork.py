import random

def verificar_intento(palabra_secreta, intento):

    resultado = ["⬛"] * len(intento)
    palabra_temp = list(palabra_secreta)

    # Verdes
    for i in range(len(intento)):
        if intento[i] == palabra_secreta[i]:
            resultado[i] = "🟩"
            palabra_temp[i] = None

    # Amarillos
    for i in range(len(intento)):
        if resultado[i] == "⬛" and intento[i] in palabra_temp:
            resultado[i] = "🟨"
            palabra_temp[palabra_temp.index(intento[i])] = None

    return resultado

def obtener_intentos(longitud):

    if longitud == 3:
        return 4

    elif longitud in [4, 5]:
        return 6

    else:
        return 8
    

def obtener_palabras_por_longitud(longitud):
    palabras ={
         3: [
         "sol", "mar", "pan", "luz", "ave", 
         "rio", "sal", "pie", "mes", "dia",
         "gol", "bar", "voz", "ley", "tos",
         "uno", "sur", "fin", "mal", "dos",
         "ojo", "feo", "rey", "pez", "gol"
         ],

        4: [
            "gato","luna","rojo","azul","cafe",
            "mesa","cama","pato","rana","nube",
            "lago","cine","rayo","roca","sopa",
            "flor","casa","leon","vaca","lago",
            "pelo","cara","boca","dado","mapa"
        ],

        5: [
            "perro","arbol","negro","verde","playa",
            "nieve","raton","mango","llave","piano",
            "reloj","tigre","limon","queso","avion",
            "cielo","campo","fruta","silla","radio",
            "juego","plaza","coche","barco","lente"
        ],

        6: [
            "tierra","viento","blanco","puerta","moneda",
            "camino","espejo","jardin","bosque","piedra",
            "fiesta","madera","helado","conejo","campos",
            "tomate","estado","anillo","trapos","mantel",
            "sombra","tesoro","pajaro","cuadro","lentes"
        ],

        7: [
            "ventana","caminos","monedas","pintura","jugador",
            "mercado","escuela","palacio","botella","peligro",
            "cerebro","trabajo","talento","pescado","abrazos",
            "motores","musical","maestro","soldado","naranja"
            "caracol","bandera","cascada","pantera","perfume"
        ]
    }
    for clave in palabras:
        palabras[clave] = [palabra.upper() for palabra in palabras[clave]]

    return palabras[longitud]


def main():
    while True:
        opcion = input("\nelegi longitud de palabra (3 a 7): ").strip()
        
        if not opcion.isdigit() or int(opcion) not in [3, 4, 5, 6, 7]:
            print("x opcion invalida")
            continue

        jugar(int(opcion))
        continuar = input("\njugar de nuevo? (s/n): ").lower().strip()
        if continuar not in ["s", "si", "sí"]:
            print("\nnos vemos chao pescao")
            break

def mostrar_menu():

    print("\n" + "=" * 50)
    print("WORDLE".center(50))
    print("=" * 50)

    print("\n1 - Fácil(para noobs) (3 letras)")
    print("2 - Normal (4 letras)")
    print("3 - Medio (5 letras)")
    print("4 - Difícil (6 letras)")
    print("5 - Experto (7 letras)")
    print("6 - Aleatorio")
    print("0 - Salir")

    while True:

        opcion = input("\nElige una opción: ")

        if opcion == "0":
            return None

        elif opcion == "1":
            return 3

        elif opcion == "2":
            return 4

        elif opcion == "3":
            return 5

        elif opcion == "4":
            return 6

        elif opcion == "5":
            return 7

        elif opcion == "6":
            return random.choice([3, 4, 5, 6, 7])

        else:
            print("❌ Opción inválida")

    
def jugar():

    longitud = mostrar_menu()

    if longitud is None:
        return None

    palabras = obtener_palabras_por_longitud(longitud)

    palabra_secreta = random.choice(palabras)

    intentos_maximos = obtener_intentos(longitud)

    intentos = 0

    letras_usadas = set()

    historial = []

    print("\n" + "=" * 50)
    print(f"PALABRA DE {longitud} LETRAS".center(50))
    print("=" * 50)

    print(f"\nTienes {intentos_maximos} intentos")

    while intentos < intentos_maximos:

        print(f"\nIntento {intentos + 1} de {intentos_maximos}")

        if letras_usadas:
            print("Letras usadas:", ", ".join(sorted(letras_usadas)))

        intento = input("\nIngresa una palabra: ").upper().strip()

        # validar la longitud de la palabra

        if len(intento) != longitud:
            print(f"❌ Debe tener {longitud} letras")
            continue

        if not intento.isalpha():
            print("❌ Solo se permiten letras")
            continue

        if intento not in palabras:
            print("❌ La palabra no existe")
            continue
        # Letras usadas 

        for letra in intento:
            letras_usadas.add(letra)

        # verificar intentos

        resultado = verificar_intento(palabra_secreta, intento)
        historial.append((intento, resultado))

      
        print()

        for palabra, res in historial:
            print(" ".join(palabra))
            print(" ".join(res))
            print()

        # mensaje al ganar

        if intento == palabra_secreta:

            print("\n" + "🎉" * 20)
            print("¡GANASTE!")
            print(f"La palabra era: {palabra_secreta}")
            print("🎉" * 20)

            return True

        intentos += 1

        restantes = intentos_maximos - intentos

        print(f"\nIntentos restantes: {restantes}")

    # mensaje al perder

    print("\n" + "😢" * 20)
    print("GAME OVER")
    print(f"La palabra era: {palabra_secreta}")
    print("😢" * 20)

    return False



def main():

    partidas_ganadas = 0
    partidas_jugadas = 0

    while True:

        resultado = jugar()

        # SALIR

        if resultado is None:

            print("\n👋 Gracias por jugar chao pescao")
            break

        partidas_jugadas += 1

        if resultado:   
            partidas_ganadas += 1

        # estadisticas del juego

        print("\n" + "=" * 40)
        print("ESTADÍSTICAS")
        print("=" * 40)

        print(f"Partidas jugadas: {partidas_jugadas}")
        print(f"Partidas ganadas: {partidas_ganadas}")

        porcentaje = int((partidas_ganadas / partidas_jugadas) * 100)

        print(f"Porcentaje de victorias: {porcentaje}%")

       

        while True:

            continuar = input("\n¿Jugar otra vez? (s/n): ").lower().strip()

            if continuar in ["s", "si", "sí"]:
                break

            elif continuar in ["n", "no"]:

                print("\n👋 Chao pescao")
                return

            else:
                print("❌ Ingresa 's' o 'n'")



if __name__ == "__main__":
    main()